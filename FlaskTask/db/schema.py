from marshmallow import (
    Schema,
    fields,
    post_dump,
)


class DriverSchema(Schema):
    short_name = fields.String()
    full_name = fields.String()
    car = fields.String()


class RaceSchema(Schema):
    start = fields.DateTime('%Y-%m-%d %H:%M:%S.%f')
    finish = fields.DateTime('%Y-%m-%d %H:%M:%S.%f')
    driver = fields.Nested(DriverSchema)
    time = fields.String()

    # @post_dump()
    # def wrap(self, data, **kwargs):
    #     key = data['driver']['short_name']
    #     return {key: {
    #         'car': data['driver']['car'],
    #         'fullname': data['driver']['full_name'],
    #         'pos': 0,
    #         'time': data['time'],
    #         'time_f': data['finish'],
    #         'time_s': data['start'],
    #     }}
