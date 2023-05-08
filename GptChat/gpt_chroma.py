import os

from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = "your-api-key"


class Chat:

    def __init__(self):
        self.persist_directory = "db"
        self.text_splitter = CharacterTextSplitter()
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = self.__init_db()

        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0
        )

        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        self.qa = ConversationalRetrievalChain.from_llm(
            self.llm,
            self.vectorstore.as_retriever(search_type="mmr"),
            memory=self.memory
        )

    def ask(self, query: str):
        result = self.qa({"question": query})
        self.__db_add(["User's question: " + result['question'], "AI answer: " + result['answer']],
                      [{"source": "Human"}, {"source": "AI"}])
        return self.__format_answer(result["answer"])

    def __init_db(self):
        """Fill db if no records while first start"""
        # Need not fewer than 20 elements to avoid Chroma exception
        vectorstore = Chroma(persist_directory=self.persist_directory, embedding_function=self.embeddings)
        exist = vectorstore.get()
        if not exist['ids']:
            loader = TextLoader("initialise_chroma.txt")
            documents = loader.load()
            text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=200, chunk_overlap=50)
            texts = text_splitter.split_documents(documents)
            vectorstore = Chroma.from_documents(
                documents=texts,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            vectorstore.persist()
        return vectorstore

    # def __init_db(self):
    #     vectorstore = Chroma(persist_directory=self.persist_directory, embedding_function=self.embeddings)
    #     exist = vectorstore.get()
    #     if not exist['ids']:
    #         documents = self.text_splitter.create_documents(
    #             ["You are a helpful assistant."],
    #             metadatas=[{"source": "System"}]
    #         )
    #         vectorstore.add_documents(documents)
    #         vectorstore.persist()
    #     return vectorstore

    def __db_add(self, texts: list[str], metadatas: list[dict] | None = None):
        documents = self.text_splitter.create_documents(texts, metadatas=metadatas)
        self.vectorstore.add_documents(documents)
        self.vectorstore.persist()

    def __format_answer(self, answer: str):
        """Format output string for print in console"""
        return f"{self.llm.model_name} answer: {answer}"


if __name__ == "__main__":
    chat = Chat()
    while True:
        user_input = input("> ")
        print(chat.ask(user_input))

#  what you think about Python?
#  write hello world on it
#  how much questions I am ask you?

#  Ask this after restart chat
#  What programming language did we talk about last time?
