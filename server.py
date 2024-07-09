import http.server
import socketserver
import os

# Set the directory you want to serve
serve_directory = os.getcwd()  # Serve the current working directory

# Ensure the directory exists
if not os.path.exists(serve_directory):
    raise FileNotFoundError(f"The directory '{serve_directory}' does not exist.")

os.chdir(serve_directory)

# Define the handler to serve files
handler = http.server.SimpleHTTPRequestHandler

# Set up the server
port = 8000
address = "0.0.0.0"

try:
    with socketserver.TCPServer((address, port), handler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Server has been shut down.")
