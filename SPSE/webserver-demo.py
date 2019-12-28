#!/usr/bin/env python
import SocketServer
import SimpleHTTPServer

class httpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/admin':
			self.wfile.write('This page is only for Admins!')
			self.wfile.write(self.headers)
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)




httpServer = SocketServer.TCPServer(('',10001),httpRequestHandler)

httpServer.serve_forever()
