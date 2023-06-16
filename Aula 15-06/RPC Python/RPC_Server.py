import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass
    def on_disconnect(self, conn):
        pass
    def exposed_add_number(self, x, y):
        return x + y
    
if __name__ == "_main_":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MyService, port=12345)
    server.start()
    print('Server on')
