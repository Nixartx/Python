from models import *
from ReportOfMonaco import ReportMonaco

with db:
    db.create_tables([Driver, Race])


if __name__ == '__main__':

    data = ReportMonaco().build_report(folder='../static/reports')
    reports = data.generate_report()
    print(reports)

    with db:
        drivers_to_insert = []
        races_to_insert = []
        for shortname in reports:
            drivers_to_insert.append(
                {
                    'id': reports[shortname]['pos'],
                    'short_name': shortname,
                    'full_name': reports[shortname]['fullname'],
                    'car': reports[shortname]['car'],
                }
            )
            races_to_insert.append(
                {
                    'start': reports[shortname]['time_s'],
                    'finish': reports[shortname]['time_f'],
                    'time': reports[shortname]['time'],
                    'driver_id': reports[shortname]['pos'],
                }
            )
        Driver.insert_many(drivers_to_insert).execute()
        Race.insert_many(races_to_insert).execute()
