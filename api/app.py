from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource
from flask_session import Session
from flask_migrate import Migrate
from api.models import db

#Initializing Flask
app=Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  
app.config["SQLALCHEMY_ECHO"] = False

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

if __name__=="__main__":
    app.run(port=5555, debug=True)