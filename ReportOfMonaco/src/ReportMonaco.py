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

        self.read_file(folder)

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

    def find_by_name_filter(self, drivername, shortname):
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

    def make_report(self, drivers_to_print, reverse=False):
        report = dict((driver, self.report[driver]) for driver in drivers_to_print)

        if not report:
            return False

        sorted_report = sorted(
            report,
            key=lambda racer: int(
                report[racer]["time"].total_seconds() *
                1000),
            reverse=reverse)

        output = {}
        for i, driver in enumerate(sorted_report, 1):
            output[driver] = report.get(driver)
            output[driver].update({'pos': i})
        return output

    def print_r(self, data, reverse=False):

        if not data:
            print("No results")
            return

        sep = 16 if not reverse else len(data) - 14
        for driver in data:
            if data[driver]['pos'] == sep:
                print("{:_^66}".format(""))
            print("{:2d}. ".format(data[driver]['pos']), end='')
            self.print_driver_info(data.get(driver))


    def prepare_data(self, folder=None, driver_name='', driver_id=''):

        if not folder:
            folder = '.'
        self.build_report(folder)

        # If driver_id not found, try to find driver_name with same value
        if driver_id:
            driver_name = self.report.get(driver_id)
            if driver_name:
                driver_name = driver_name['fullname']
            else:
                driver_name = driver_id

        drivers_to_print = list(
            filter(
                lambda x: self.find_by_name_filter(
                    drivername=driver_name,
                    shortname=x),
                self.report))
        return drivers_to_print

    def print_report(self, folder=None, driver_name='', driver_id='', reverse=False):
        '''
        The entry point for working with the class. Depending on the parameters, it works with the racer report.
        :param folder: string path to folder with reports
        :param driver_name: Driver name for printing report by this racer
        :param driver_id: Driver short name for printing report by this racer
        :param reverse: ASC or DESC sorting report
        :return: None
        '''
        drivers_to_print = self.prepare_data(folder=folder, driver_name=driver_name, driver_id=driver_id)
        data = self.make_report(drivers_to_print, reverse=reverse)
        self.print_r(data, reverse=reverse)

    def get_report(self, folder=None, driver_name='', driver_id='', reverse=False):
        drivers_to_print = self.prepare_data(folder=folder, driver_name=driver_name, driver_id=driver_id)
        return self.make_report(drivers_to_print, reverse=reverse)

    def generate_report(self, driver_name='', driver_id='', reverse=False):
        # If driver_id not found, try to find driver_name with same value
        if driver_id:
            driver_name = self.report.get(driver_id)
            if driver_name:
                driver_name = driver_name['fullname']
            else:
                driver_name = driver_id

        drivers_to_print = list(
            filter(
                lambda x: self.find_by_name_filter(
                    drivername=driver_name,
                    shortname=x),
                self.report))

        report = dict((driver, self.report[driver]) for driver in drivers_to_print)

        if not report:
            return False

        sorted_report = sorted(
            report,
            key=lambda racer: int(
                report[racer]["time"].total_seconds() *
                1000),
            reverse=reverse)

        output = {}
        for i, driver in enumerate(sorted_report, 1):
            output[driver] = report.get(driver)
            output[driver].update({'pos': i})
        return output
