from http.server import HTTPServer,BaseHTTPRequestHandler

class Index(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Contenty-type", "text/html")
        self.end_headers()
        self.wfile.write("<h1>Hello World!</h1><button>Click Aqui</button>".encode("utf=8"))

app = HTTPServer(("0.0.0.0",8000),Index)
app.serve_forever()
