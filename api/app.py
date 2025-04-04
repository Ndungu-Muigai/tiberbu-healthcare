from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource
from flask_session import Session
from flask_migrate import Migrate
from api.models import db, Pateint, NexOfKin, Doctor, Appointment
from schema import NextOfKinSchema, PatientSchema, DoctorSchema, AppointmentSchema

#Initializing Flask
app=Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  
app.config["SQLALCHEMY_ECHO"] = False

#Session configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

#Initializing the migrations
migrate=Migrate(app, db)
db.init_app(app)

#Intializing the API
api=Api(app)

#Initializing the session
Session(app)

#Index resource
class Index(Resource):
    def get(self):
        return {"message": "Welcome to the Tiberbu Healthcare API"}
    
api.add_resource(Index, "/")

#Doctors resource
class Doctors(Resource):
    def get(self):

        #Getting the doctors details from the database
        all_doctors=Doctor.query.all()

        #Creating a JSON for the doctors details to send to the frontend
        doctors_details=DoctorSchema(many=True).dump(all_doctors)

        #Creating a response 
        return make_response(jsonify(
            {
                "type": "success",
                "doctors" : doctors_details
            }
        ), 200)
    
    def post(self):

        #Getting the data from the request
        data=request.get_json()
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        email=data.get("email")
        phone_number=data.get("phone_number")
        department=data.get("department")

        #Checking if an account with the same email exists
        if Doctor.query.filter_by(email=email).first():
            return make_response(jsonify(
                {
                    "type" : "error",
                    "message" : "An account with this email already exists"
                }
            ), 409)

        #Inserting the data into the database
        new_doctor=Doctor(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number, department=department)
        db.session.add(new_doctor)
        db.session.commit()

        #Creating a response
        return make_response(jsonify(
            {
                "type" : "success",
                "message" : "Doctor added successfully"
            }
        ), 201)

api.add_resource(Doctors, "/doctors")

if __name__=="__main__":
    app.run(port=5555, debug=True)