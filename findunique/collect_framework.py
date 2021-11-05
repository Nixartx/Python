from findunique import CountUnique
import argparse


class CLCountUnique(CountUnique):
    __parser = 0
    __args = 0

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser.add_argument("--string", type=str)
        self.__parser.add_argument("--file", type=str, help="Path to file")

    def __readfile(self):
        f = open(self.__args.file)
        lines = f.readlines()
        f.close()
        return lines

    def run(self, args=0):
        if args:
            self.__args = self.__parser.parse_args(args)
        else:
            self.__args = self.__parser.parse_args()

        if self.__args.file:
            for key, line in enumerate(self.__readfile()):
                print(
                    "Строка: {0}. Уникальных символов: {1}".format(
                        key + 1, self.count(line)))
        elif self.__args.string:
            print(
                "Уникальных символов: {0}".format(
                    self.count(
                        self.__args.string)))

# if __name__ == '__main__':
#     CLCountUnique().run(["--file", "../FilesForTests/text.txt"])
