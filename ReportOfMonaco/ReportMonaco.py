import datetime


class ReportMonaco:

    def __init__(self):
        self.data = dict.fromkeys(["start", "finish", "abbreviations"])
        self.report = {}

    def readfile(self, folder):

        files = {
            "start": "start.log",
            "finish": "end.log",
            "abbreviations": "abbreviations.txt",
        }
        for key, value in files.items():
            with open(folder + "/" + value) as f:
                self.data[key] = [line.strip() for line in f.readlines()]
        return self.data

    def build_report(self, folder='.'):
        self.readfile(folder)
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
        if driver:
            print(
                "{:<20} | {:<25} | {:<10}".format(
                    driver["fullname"], driver["car"], str(
                        driver["time"])[
                        :-3]))
        else:
            print("No results")

    def find_by_name(self, name):
        for driver in self.report.values():
            if driver["fullname"].upper() == name.upper():
                return driver
        return False

    def list_all(self, reverse=False):
        sorted_report = sorted(
            self.report,
            key=lambda racer: int(
                self.report[racer]["time"].total_seconds() *
                1000),
            reverse=reverse)
        sep = 16 if not reverse else len(sorted_report) - 14
        for i, driver in enumerate(sorted_report, 1):
            if i == sep:
                print("{:_^66}".format(""))
            print("{:2d}. ".format(i), end='')
            self.print_driver_info(self.report[driver])

    def print_report(self, folder=None, driver_name='', reverse=False):
        if not folder:
            folder = '.'
        self.build_report(folder)
        if driver_name:
            self.print_driver_info(self.find_by_name(driver_name))
        else:
            self.list_all(reverse)


if __name__ == "__main__":
    ReportMonaco().print_report(folder='reports', driver_name="Daniel Ricciardo")
    # rep.print_report(False)
    # rep.print_report("Daniel Ricciardo")
