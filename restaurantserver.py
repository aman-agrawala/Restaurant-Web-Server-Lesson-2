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