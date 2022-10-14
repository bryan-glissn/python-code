import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
USERNAME="Jill"
# host = "41.60.232.142"
# host = socket.gethostbyname(socket.gethostname())
host = "127.0.0.1"
# host = external_IP('0.0.0.0')
port = 9011
# host = target_host
# port = target_port

client.connect((host, port))
client.send(USERNAME.encode())
while True:

    print("waiting for response")
    server_messg = client.recv(30)
    print(server_messg.decode())
    client_messg = input("send message to server: ")
    client.send(f"{USERNAME}: {client_messg}".encode())
