from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Pateint(db.Model):

    __tablename__ = "patients"

    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False, unique=True)
    phone_number=db.Column(db.String, nullable=False)
    gender=db.Column(db.Enum("Male", "Female", name="gender_enum"), nullable=False)
    dob=db.Column(db.DateTime, nullable=False)
    insurance_name=db.Column(db.String, nullable=False)
    insurance_number=db.Column(db.String, nullable=False)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    #Creating the relationships to other tables
    kins=db.relationship("NextOfKin", backref="patient", uselist=True)
    appointments=db.relationship("Appointment", backref="patient", uselist=True)

class NexOfKin(db.Model):

    __tablename__ = "kins"
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False, unique=True)
    phone_number=db.Column(db.String, nullable=False)
    relationship=db.Column(db.String, nullable=False)
    patient_id=db.Column(db.Integer, db.ForeignKey("patients.id"))
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

class Doctor(db.Model):

    __tablename__ = "doctors"
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False, unique=True)
    phone_number=db.Column(db.String, nullable=False)
    department=db.Column(db.String, nullable=False)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    #Creating the relationships
    appointments=db.relationship("Appointment", backref="doctor", uselist=True)

class Appointment(db.Model):

    __tablename__ = "appointments"
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.DateTime, nullable=False)
    time=db.Column(db.DateTime, nullable=False)
    patient_id=db.Column(db.Integer, db.ForeignKey("patients.id"))
    doctor_id=db.Column(db.Integer, db.ForeignKey("doctors.id"))
    status=db.Column(db.Enum("Scheduled", "Completed", "Cancelled", name="status_enum"), nullable=False)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())