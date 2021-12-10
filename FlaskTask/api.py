import json
import os
from simplexml import dumps
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flasgger import Swagger
from FlaskTask.db.models import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Create an APISpec
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Flask Restful Swagger",
            "description": "Flask Restful Swagger",
            "version": "1.0",
            "contact": {
                "name": "Nixart",
            }
        },
    }

    app.config['SWAGGER'] = {
        'title': 'Report Of Monaco API',
        'uiversion': 3,
        "specs_route": "/api/v1/swagger/"
    }

    swagger = Swagger(app, template=template)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=db
    )


    api = Api(app)


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

    # data = ReportMonaco().build_report(folder='static/reports')

    def convert_to_dict(data):
        reports = {}
        for row in data:
            reports.update({row.driver_id.short_name: {
                'car': row.driver_id.car,
                'fullname': row.driver_id.full_name,
                'pos': row.driver_id.id,
                'time': row.time,
                'time_f': row.finish,
                'time_s': row.start,
            }})
        return reports

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
            """
                 get endpoint
                 ---
                 tags:
                   - Report of Monaco APIs
                 produces:
                    - "application/json"
                    - "application/xml"
                 parameters:
                   - name: driver_id
                     in: query
                     type: string
                     required: false
                     description: id of driver ("SVF")
                   - name: order
                     in: query
                     type:
                     enum: [asc, desc]
                     required: false
                     description: sorting "asc" or "desc"
                 responses:
                   200:
                     description: List of drivers
                     schema:
                       type: object
                       properties:
                         driver_id:
                           type: object
                           description: short name of driver
                           properties:
                            car:
                                type: string
                                description: car
                            fullname:
                                type: string
                                description: name of driver
                            pos:
                                type: integer
                                description: position by time in table
                            time:
                                type: timedelta
                                description: race time result
                            time_f:
                                type: datetime
                                description: finish time
                            time_s:
                                type: datetime
                                description: start time
                           description: list of drivers
                 """
            driver_id = request.args.get('driver_id')
            order = request.args.get('order', 'asc')
            reverse = order.upper() == 'DESC'
            if driver_id:
                reports = Race.select(
                    Race.start,
                    Race.finish,
                    Race.time,
                    Driver.short_name,
                    Driver.full_name,
                    Driver.car,
                    Driver.id
                ).join(Driver).where(Driver.short_name == driver_id).order_by(Race.time)
                return convert_to_dict(reports)

            reports = Race.select().join(Driver).order_by(Race.time)
            return convert_to_dict(reports)

    api.add_resource(Report, '/api/v1/report/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
