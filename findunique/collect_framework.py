from findunique import CountUnique
import argparse


class CLCountUnique(CountUnique):
    parser = 0
    _args = 0

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--string", type=str)
        self.parser.add_argument("--file", type=str, help="Path to file")

    def readfile(self):
        with open(self._args.file) as f:
            lines = f.readlines()
        return lines

    def run(self, args=None):
        try:
            self._args = self.parser.parse_args(args)
            if self._args.file:
                for key, line in enumerate(self.readfile(), 1):
                    print(
                        "Строка: {0}. Уникальных символов: {1}".format(
                            key, self.count(line)))
            elif self._args.string:
                print(
                    "Уникальных символов: {0}".format(
                        self.count(
                            self._args.string)))
        except FileNotFoundError:
            print("Error: File does not appear to exist.")

if __name__ == "__main__":
    CLCountUnique().run(['--file', 'abc'])