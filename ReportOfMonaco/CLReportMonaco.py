import argparse
from ReportMonaco import ReportMonaco

class CLReportMonaco(ReportMonaco):
    parser = 0
    def __init__(self):

        self.parser = argparse.ArgumentParser()

        group = self.parser.add_argument_group('group',"use [--asc | --desc] flag")
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument("--asc", dest='reverse', help="By default", action='store_false')
        group.add_argument("--desc", dest='reverse', action='store_true')
        group.set_defaults(reverse=False)

        self.parser.add_argument("--files", type=str, help="Folder with files")
        self.parser.set_defaults(driver_case=False)

        subparsers = self.parser.add_subparsers()
        parser_driver=subparsers.add_parser('driver')
        parser_driver.add_argument('drivername', help='Name of driver')
        parser_driver.set_defaults(driver_case=True)

        super().__init__()

    def run(self, args_custom=None):
        args = self.parser.parse_args(args_custom)
        if args.driver_case:
            self.print_report(folder=args.files,driver_name=args.drivername)
        else:
            self.print_report(folder=args.files,reverse = args.reverse)
