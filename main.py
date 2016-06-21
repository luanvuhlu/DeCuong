# -*- coding: utf-8 -*- 
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


BASE_PATH = os.path.dirname(__file__)

class About(webapp.RequestHandler):
    def get(self, *args):
        path = os.path.join(BASE_PATH, 'templates/index.html')
        template_values = {
                           
                           }
        self.response.out.write(template.render(path, template_values ))
application = webapp.WSGIApplication([
                                      ('/', About),
                                    ], debug=True)
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()
