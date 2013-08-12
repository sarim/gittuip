import webapp2
import os

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Your IP: ')
        self.response.write(os.environ['REMOTE_ADDR'] )


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=False)
