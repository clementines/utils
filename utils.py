# EASY SERVE of HTML and CSS
# python -m http.server --directory ../web2/

import http.server
import socketserver
import os
# import functools

PORT = 8000
web_dir = '../web2/'

os.chdir(web_dir)
cwd = os.getcwd()

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("serving contents of", cwd)
    httpd.serve_forever()