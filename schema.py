from marshmallow import Schema, fields

class NextOfKinSchema(Schema):
    id=fields.Integer(required=True)
    first_name=fields.String(required=True)
    last_name=fields.String(required=True)
    email=fields.String(required=True)
    phone_number=fields.String(required=True)
    relationship=fields.String(required=True)

class PatientSchema(Schema):
    id=fields.Integer(required=True)
    first_name=fields.String(required=True)
    last_name=fields.String(required=True)
    email=fields.String(required=True)
    phone_number=fields.String(required=True)
    gender=fields.String(required=True)
    dob=fields.Date(required=True)
    insurance_name=fields.String(required=True)
    insurance_number=fields.String(required=True)

    next_of_kin=fields.Nested(NextOfKinSchema)

class DoctorSchema(Schema):
    id=fields.Integer(required=True)
    first_name=fields.String(required=True)
    last_name=fields.String(required=True)
    email=fields.String(required=True)
    phone_number=fields.String(required=True)
    department=fields.String(required=True)

class AppointmentSchema(Schema):
    id=fields.Integer(required=True)
    date=fields.Date(required=True)
    time=fields.Time(required=True)
    doctor=fields.Nested(DoctorSchema)
    patient=fields.Nested(PatientSchema)
    status=fields.String(required=True)