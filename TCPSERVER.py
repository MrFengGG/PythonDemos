from socketserver import TCPServer,StreamRequestHandler,ThreadingMixIn

class Server(ThreadingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('获得连接',addr)
        self.wfile.write('hellow client'.encode())
server = TCPServer(('',1234),Handler)
server.serve_forever()
