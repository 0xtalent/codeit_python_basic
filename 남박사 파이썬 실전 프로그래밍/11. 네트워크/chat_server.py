import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("", 12000), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()