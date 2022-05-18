import cherrypy, json, sys

from predict import Prediction

a = None

class WebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def duplicates(self):
      data = cherrypy.request.json
      print (data)
      output = {}
      threshold = data.get("threshold", 0.8)

      if "id" in data.keys():
         output = a.runById(data["id"])

      if "url" in data.keys():
         output = a.runByUrl(data["url"])

      if "text" in data.keys():
         output = a.runByText(data["text"], threshold)

      return output


if __name__ == '__main__':

   a = Prediction()

   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(WebService())	