import Pyro4

@Pyro4.expose

class MyService(object):
    def add_numbers(self,x,y):
        return x + y
    
daemon = Pyro4.Daemon()
uri = daemon.register(MyService)
print("URI Disponível: ",uri)

daemon.requestLoop()