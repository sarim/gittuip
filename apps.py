from bottle import get,redirect,template,request, response, default_app, run, debug
import os

@get("/")
def index():
    response.set_header('Content-Type', 'text/html')
    ip = os.environ['REMOTE_ADDR']
    browser = request.headers.get("User-Agent")
    if browser.startswith("Mozilla/"):
        redirect("/details")
    return "Your IP : %s" % ip

@get("/details")
def details():
    ip = os.environ['REMOTE_ADDR']
    ret = {"REMOTE_ADDR" : ip}
    for key in request.headers:
        ret[key] = request.headers.get(key)
    
    return template("template", data=ret)


application = default_app()
if __name__=="__main__":
    debug(True)
    run(port = 8990)