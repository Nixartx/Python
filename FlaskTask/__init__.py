import os
from flask import Flask, render_template, request, redirect, url_for
from ReportOfMonaco import ReportMonaco


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('test_config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    data = ReportMonaco().build_report(folder='static/reports')

    # routes
    @app.route('/', methods=['GET'])
    def index():
        return redirect(url_for('report'))


    @app.route('/report/', methods=['GET'])
    def report():
        order = request.args.get('order', 'asc')
        reverse = order.upper() == 'DESC'

        reports = data.generate_report(reverse=reverse)
        return render_template('report.html', data=reports)

    @app.route('/report/drivers/', methods=['GET'])
    def list():
        driver_id = request.args.get('driver_id')
        order = request.args.get('order')
        if order and order.upper() == 'DESC':
            order = True
        else:
            order = False

        if driver_id:
            reports = data.generate_report(
                driver_id=driver_id,
                reverse=order)
            return render_template('report.html', data=reports)

        reports = data.generate_report(reverse=order)
        return render_template('list.html', data=reports)

    @app.template_filter()
    def format_datetime(value):
        return str(value)[:-3]

    return app
