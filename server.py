from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
from db_utils import *

def get_data(request):
    data = exec_get_all("SELECT * from test")
    result = {}
    for entry in data:
        result[entry[0]] = {
            "id": entry[0],
            "name": entry[1]
        }
    return Response(str(result))

def test_route(request):
    return Response("testing")
    
if __name__ == '__main__':
    # port = int(os.environ.get("PORT"))
    port = 8080
    with Configurator() as config:
        config.add_route('data', '/')
        config.add_view(get_data, route_name='data')
        config.add_route('test', '/test')
        config.add_view(test_route, route_name='test')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app) #for deployment ONLY - comment out while testing locally
    # server = make_server('127.0.0.1', port, app) #for local testing ONLY - comment out before pushing
    server.serve_forever()