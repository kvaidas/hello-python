import http.server


class GetRoot(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes('Hello', encoding='ascii'))


server = http.server.HTTPServer(('', 80), GetRoot)
server.serve_forever()
