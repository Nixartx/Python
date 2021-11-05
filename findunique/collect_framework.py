from findunique import CountUnique
import argparse


class CLCountUnique(CountUnique):
    parser = 0

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--string", type=str)
        self.parser.add_argument("--file", type=str, help="Path to file")

    def readfile(self, file):
        with open(file) as f:
            lines = f.readlines()
        return lines

    def run(self, args_custom=None):
        args = self.parser.parse_args(args_custom)
        if args.file:
            try:
                lines = self.readfile(args.file)
            except FileNotFoundError:
                print("Error: File does not appear to exist.")
                exit()
            for key, line in enumerate(lines, 1):
                print(
                    "Строка: {0}. Уникальных символов: {1}".format(
                        key, self.count(line)))
        elif args.string:
            print(
                "Уникальных символов: {0}".format(
                    self.count(
                        args.string)))


if __name__ == "__main__":
    CLCountUnique().run(['--file', 'abc'])
