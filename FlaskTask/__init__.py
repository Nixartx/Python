import os
from flask import Flask, render_template, request
from ReportOfMonaco import ReportMonaco


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # routes
    @app.route('/', methods=['GET'])
    @app.route('/report/', methods=['GET'])
    def report():
        order = request.args.get('order')
        if order and order.upper() == 'DESC':
            order = True
        else:
            order = False

        data = ReportMonaco().print_report(folder='static/reports', reverse=order)
        return render_template('report.html', data=data)

    @app.route('/report/drivers/', methods=['GET'])
    def list():
        driver_id = request.args.get('driver_id')
        order = request.args.get('order')
        if order and order.upper() == 'DESC':
            order = True
        else:
            order = False

        if driver_id:
            # Finds full name of driver
            rmobj = ReportMonaco().build_report('static/reports')
            driver_name = rmobj.report.get(driver_id)['fullname']

            data = rmobj.print_report(
                folder='static/reports',
                driver_name=driver_name,
                reverse=order)
            return render_template('report.html', data=data)

        data = ReportMonaco().print_report(folder='static/reports', reverse=order)
        return render_template('list.html', data=data)

    @app.template_filter()
    def format_datetime(value):
        return str(value)[:-3]

    return app
