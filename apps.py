from bottle import get,redirect,template,request, response, default_app, run, debug
import os

@get("/")
def index():
    response.set_header('Content-Type', 'text/html')
    #os.environ['REMOTE_ADDR']
    return str(os.environ)

application = default_app()
if __name__=="__main__":
    debug(True)
    run(port = 8990)