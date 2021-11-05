from findunique import CountUnique
import argparse


class CLCountUnique(CountUnique):
    __parser = 0
    __args = 0

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser.add_argument("--string", type=str)
        self.__parser.add_argument("--file", type=str, help="Path to file")

    def readfile(self):

            with open(self.__args.file) as f:
                lines = f.readlines()
            return lines


    def run(self, args=None):
        try:
            self.__args = self.__parser.parse_args(args)
            if self.__args.file:
                for key, line in enumerate(self.readfile(), 1):
                    print(
                        "Строка: {0}. Уникальных символов: {1}".format(
                            key, self.count(line)))
            elif self.__args.string:
                print(
                    "Уникальных символов: {0}".format(
                        self.count(
                            self.__args.string)))
        except FileNotFoundError:
            print("Error: File does not appear to exist.")

if __name__ == "__main__":
    CLCountUnique().run(['--file', 'abc'])