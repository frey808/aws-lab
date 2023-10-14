from flask import Flask
from flask_restful import Resource, Api

from server.api.skate import *
from server.db.setup import *

app = Flask(__name__) #create Flask instance
api = Api(app) #api router

api.add_resource(Data,'/')

if __name__ == '__main__':
    print("Loading db")
    rebuild()
    print("Starting flask")
    app.run(debug=True)