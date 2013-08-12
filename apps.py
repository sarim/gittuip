from bottle import get,redirect,template,response, default_app
import os

@get("/")
def index(self):
    response.set_header('Content-Type', 'text/html')
    #os.environ['REMOTE_ADDR']
    return request.headers


application = default_app()