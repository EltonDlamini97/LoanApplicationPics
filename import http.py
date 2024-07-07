import http.server
import socketserver
import os

# Set the directory you want to serve
os.chdir("Images")

# Define the handler to serve files
handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("0.0.0.0", 8000), handler) as https:
    print("Serving at port 8000")
    https.serve_forever()