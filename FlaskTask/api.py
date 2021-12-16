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
    app.config.from_object('config.Config')
    api = Api(app)

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

    db = SqliteDatabase(app.config['DATABASE'])

    # app.config.from_mapping(
    #     SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
    #     DATABASE=db,
    # )



    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def convert_to_dict(data):
        reports = {}
        for i, row in enumerate(data, 1):
            reports.update({row.driver.short_name: {
                'car': row.driver.car,
                'fullname': row.driver.full_name,
                'pos': i,
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

            reports = Race.select(
                Race.start,
                Race.finish,
                Race.time,
                Driver.short_name,
                Driver.full_name,
                Driver.car,
            ).join(Driver)
            if reverse:
                reports = reports.order_by(Race.time.desc())
            else:
                reports = reports.order_by(Race.time.asc())

            if driver_id:
                reports = reports.where(Driver.short_name == driver_id)
                return convert_to_dict(reports)
            return convert_to_dict(reports)

    api.add_resource(Report, '/api/v1/report/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
