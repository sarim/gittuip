from bottle import get,redirect,template,response, default_app, run, debug
import os

@get("/")
def index(self):
    response.set_header('Content-Type', 'text/html')
    #os.environ['REMOTE_ADDR']
    return request.headers

debug(True)
application = default_app()
run(server="gae")