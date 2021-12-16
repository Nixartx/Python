from ReportOfMonaco import ReportMonaco
from FlaskTask.db.models import db, Race, Driver


def create_db(db_path=None):
    if db_path:
        db.init(db_path)
    with db:
        db.create_tables([Driver, Race])


def parse_data_to_db(report_folder_path, db_path=None):
    if db_path:
        db.init(db_path)

    data = ReportMonaco().build_report(folder=report_folder_path)
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
                    'driver': reports[shortname]['pos'],
                }
            )
        Driver.insert_many(drivers_to_insert).execute()
        Race.insert_many(races_to_insert).execute()


if __name__ == '__main__':
    create_db('monaco.db')
    parse_data_to_db('../static/reports','monaco.db')

