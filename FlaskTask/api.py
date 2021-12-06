import json
import os
from simplexml import dumps
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from ReportOfMonaco import ReportMonaco


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
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

    data = ReportMonaco().build_report(folder='static/reports')

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        resp = make_response(json.dumps({'response': data}, default=str), code)
        resp.headers.extend(headers or {})
        return resp


    @api.representation('application/xml')
    def output_xml(data, code, headers=None):
        resp = make_response(dumps({'response': data}), code)
        resp.headers.extend(headers or {})
        return resp


    class Report(Resource):
        def get(self):
            driver_id = request.args.get('driver_id')
            order = request.args.get('order', 'asc')
            reverse = order.upper() == 'DESC'
            if driver_id:
                reports = data.generate_report(
                    driver_id=driver_id,
                    reverse=reverse)
                return reports
            reports = data.generate_report(reverse=reverse)
            return reports

    api.add_resource(Report, '/api/report/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
