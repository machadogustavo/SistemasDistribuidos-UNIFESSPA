import rpyc

if __name__ == "_main_":
    conn = rpyc.connect("localhost", 12345)
    remote_service = conn.root

    result = remote_service.add_numbers(4, 4)
    print("O resultado:", result)

    conn.close()