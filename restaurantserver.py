# Webserver imports
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# SQL ALchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession() 

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				restaurants = session.query(Restaurant).all()
				output = '<html><body>'
				output += '<h2><a href = "/restaurants/new">Make a New Restaurant Here</a></h2>'

				for restaurant in restaurants:
					output += "<h2>%s<h2>" % restaurant.name
					output += "<ul><li><a href = '/restaurants/%s/edit'>Edit</a></li>" % restaurant.id
					output += "<li><a href = 'restaurants/%s/delete'>Delete</a></li></ul>" % restaurant.id
					#print output # for debugging

				output += "</body></html>"
				self.wfile.write(output) # send output back to client
				return # exit if statement
		except IOError:
			self.send_error(404, "File Not Found: %s" % self.path)
		



def main():
	try:
		port = 8080
		server = HTTPServer(('',port), Handler)
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping webserver..."
		server.socket.close()

if __name__ == '__main__':
	main()