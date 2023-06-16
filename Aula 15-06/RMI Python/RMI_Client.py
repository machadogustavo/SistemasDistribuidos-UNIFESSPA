import Pyro4

uri = "PYRO:obj_123455@localhost:59455"

remote_service = Pyro4.Proxy(uri)

result = remote_service.add_numbers(3,3)

print("Resultado: ",result)



