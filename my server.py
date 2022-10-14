i socketmport
import threading

server = sockesocket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
# host = target_host
# port = target_port
# host = "41.60.232.142"
# host = "192.168.88.112"
port = 9011

server.bind((host, port))
no_of_clients = 0
client_names = []
server.listen()
print(threading.active_count())

print(f"[LISTENING] server is listening..{host}:{port} for connection")


# conn, addr = server.accept()
# print("connected with ", addr)


def accept_requests(conn, addr):
    global no_of_clients
    global client_names
    name = conn.recv(30).decode()
    client_names.append(name)
    print(f"Connected with {name}: {addr[0]}")
    online = True
    no_of_clients = threading.active_count() - 1
    while online:
        # server.connect((target_host, target_port))
        # TODO: work on three clients
        message = input(f"Reply to {client_names[client_names.index(name) -1]}: ")
        conn.send(f"Server: {message}".encode())
        print("waiting for response")
        client_messg = conn.recv(1024)
        print(client_messg.decode())


# while True:
#     pass
# message = input("reply to client: ")
# conn.send(message.encode())
# print("waiting for response")
# client_messg = conn.recv(1024)
# print("message from client: ", client_messg.decode())

while True:
    # print("1111")
    c, a = server.accept()
    # print("2222")
    new_client = threading.Thread(target=accept_requests, args=(c, a))
    # print("3333")
    new_client.start()
    # print("4444")
