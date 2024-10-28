from marshmallow import Schema, fields


class ServiceTicketSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    expertise = fields.Str(required=True)
    years_of_experience = fields.Int(required=True)

class CreateServiceTicketSchema(Schema):
    name = fields.Str(required=True)
    expertise = fields.Str(required=True)
    years_of_experience = fields.Int(required=True)

class UpdateServiceTicketSchema(Schema):
    name = fields.Str()
    expertise = fields.Str()
    years_of_experience = fields.Int()