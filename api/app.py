from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource
from flask_session import Session
from flask_migrate import Migrate
from api.models import db

#Initializing Flask
app=Flask(__name__)

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