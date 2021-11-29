import argparse
from ReportOfMonaco import ReportMonaco


class CLReportMonaco(ReportMonaco):
    '''
    Сlass extends CountUnique for working with the command line.

    Example of usage:

        CLCountUnique().run(['--files', 'reports'])

        CLCountUnique().run(['--files', 'reports', '--desc'])

        CLCountUnique().run(['--files', 'reports', 'driver', 'Daniel Ricciardo'])
    '''

    parser = 0

    def __init__(self):
        '''
        init argparse groups and variables

        group:
        keys: --asc,---desc are flags True/False for variable reverse with default value False

        --files - path to folder with reports

        Subparser "driver" with param drivername

        For work with parser and subparser uses default variable "driver_case"
        '''

        self.parser = argparse.ArgumentParser()

        group = self.parser.add_argument_group(
            'group', "use [--asc | --desc] flag")
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument(
            "--asc",
            dest='reverse',
            help="By default",
            action='store_false')
        group.add_argument("--desc", dest='reverse', action='store_true')
        group.set_defaults(reverse=False)

        self.parser.add_argument("--files", type=str, help="Folder with files")
        self.parser.set_defaults(driver_case=False)

        subparsers = self.parser.add_subparsers()
        parser_driver = subparsers.add_parser('driver')
        parser_driver.add_argument('drivername', help='Name of driver')
        parser_driver.set_defaults(driver_case=True)

        super().__init__()

    def run(self, args_custom=None):
        '''
        The entry point for working with the class.
        Depending on the driver_case variable, one of the scenarios works

        Usage example:

        CLReportMonaco().run()

        CLReportMonaco().run(['--files', 'reports', 'driver', 'Daniel Ricciardo'])

        :param args_custom: command line args
        :return: False
        '''
        args = self.parser.parse_args(args_custom)
        if args.driver_case:
            self.print_report(folder=args.files, driver_name=args.drivername)
        else:
            self.print_report(folder=args.files, reverse=args.reverse)
