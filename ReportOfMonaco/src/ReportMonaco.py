import datetime
from pathlib import Path


class ReportMonaco:
    '''
    Class for working with the report of the Monaco 2018 Racing. To work, you need three report files:
    start.log, end.log, abbreviations.txt
    Example of using:
    ReportMonaco().print_report(folder='reports')
    or
    ReportMonaco().print_report(folder='reports', driver_name="Daniel Ricciardo")
    '''

    def __init__(self):
        '''Init dict data attribute with data from files and dict report with processed data'''
        self.data = dict.fromkeys(["start", "finish", "abbreviations"])
        self.report = {}

    def read_file(self, folder):
        '''Makes the file path from the user's folder param and reads the files into self.data'''
        files = {
            "start": "start.log",
            "finish": "end.log",
            "abbreviations": "abbreviations.txt",
        }
        for key, value in files.items():
            path = Path.cwd() / folder / value
            with open(path) as f:
                self.data[key] = [line.strip() for line in f.readlines()]
        return self.data

    def build_report(self, folder='.'):
        '''
        Makes a dictionary with a key that is an abbreviation of the driver and value is dictionary with all
        information about the driver collected from the report files
        :param folder: path to folder with files
        :return: self
        '''
        # try:
        self.read_file(folder)
        # except FileNotFoundError:
        #     print("Error: File does not appear to exist.")
        #     exit()
        racers = {}
        for row in self.data["start"]:
            if row:
                row += "PM"
                racers[row[:3]] = {"time_s": datetime.datetime.strptime(
                    row[3:], '%Y-%m-%d_%I:%M:%S.%f%p')}

        for row in self.data["finish"]:
            if row:
                row += "PM"
                racers[row[:3]].update(
                    {"time_f": datetime.datetime.strptime(row[3:], '%Y-%m-%d_%I:%M:%S.%f%p')})

        for row in self.data["abbreviations"]:
            if row:
                tmp = row.split("_")
                racers[tmp[0]].update({"fullname": tmp[1], "car": tmp[2]})

        for racer in racers.values():
            racer.update({"time": racer["time_f"] - racer["time_s"]})

        self.report = racers
        return self

    def print_driver_info(self, driver):
        '''
        Prints row with driver info
        :param driver: is a dict with info about driver. Keys: fullname, car, time
        :return:
        '''
        if driver:
            print(
                "{:<20} | {:<25} | {:<10}".format(
                    driver["fullname"], driver["car"], str(
                        driver["time"])[
                        :-3]))
        else:
            print("No results")
        return driver

    def find_ny_name_filter(self, drivername, shortname):
        '''
        Filter function that looking for a driver by name. If drivername doesn't pass, return True to all
        :param drivername: string that user entered
        :param shortname: short code of driver and key in self.report dict, that pass from filter() called
        :return: True if it find driver or driver doesn't pass. False in other cases
        '''
        if not drivername or self.report[shortname]["fullname"].upper(
        ) == drivername.upper():
            return True
        return False

    def list_all(self, drivers_to_print, reverse=False):
        '''
        Generate dict report from self.report with drivers witch need to be printed
        Prints report for all drivers from self.report dict
        :param reverse: ASC or DESC sort report
        :param drivers_to_print list of drivers witch need to be printed
        :return: None
        '''

        report = dict((driver, self.report[driver])
                      for driver in drivers_to_print)

        if not report:
            print("No results")
            return

        output={}
        sorted_report = sorted(
            report,
            key=lambda racer: int(
                report[racer]["time"].total_seconds() *
                1000),
            reverse=reverse)
        sep = 16 if not reverse else len(sorted_report) - 14
        for i, driver in enumerate(sorted_report, 1):
            if i == sep:
                print("{:_^66}".format(""))
            print("{:2d}. ".format(i), end='')
            output[driver]=(self.print_driver_info(report.get(driver)))
            output[driver].update({'pos':i})
        return output

    def print_report(self, folder=None, driver_name='', reverse=False):
        '''
        The entry point for working with the class. Depending on the parameters, it works with the racer report.
        :param folder: string path to folder with reports
        :param driver_name: Driver name for printing report by this racer
        :param reverse: ASC or DESC sorting report
        :return: None
        '''
        if not folder:
            folder = '.'
        self.build_report(folder)
        drivers_to_print = list(
            filter(
                lambda x: self.find_ny_name_filter(
                    drivername=driver_name,
                    shortname=x),
                self.report))

        out=self.list_all(drivers_to_print, reverse=reverse)
        return out
