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
    ret = ["Your IP : %s" % ip]
    for key in request.headers:
        line = "%s : %s" % (key , request.headers.get(key))
        ret.append(line)
    
    return "<br>".join(ret)


application = default_app()
if __name__=="__main__":
    debug(True)
    run(port = 8990)