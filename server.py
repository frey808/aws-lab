from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "hello, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
    
# from flask import Flask
# from flask_restful import Resource, Api

# from server.api.resources import *
# from server.db.setup import *

# app = Flask(__name__) #create Flask instance
# api = Api(app) #api router

# api.add_resource(Data,'/')
# api.add_resource(Edit,'/edit')

# if __name__ == '__main__':
#     print("Loading db")
#     rebuild()
#     print("Starting flask")
#     app.run(debug=True)