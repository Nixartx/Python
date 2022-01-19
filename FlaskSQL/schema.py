from marshmallow import (
    Schema,
    fields,
)


class GroupSchema(Schema):
    id = fields.Integer()
    name = fields.String()


class StudentSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    group_id = fields.Nested(GroupSchema)


class ScheduleSchema(Schema):
    course_id = fields.Integer()
    student_id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
