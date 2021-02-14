import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tup1 = "localhost", 12345
sock.bind(("localhost", 12345))
sock.listen(10)
socket1, addr1 = sock.accept()
print("Accepted connection from ", addr1)

data = socket1.recv(1024)
if data:
    print("Received Bytes: ", len(data))
    send = socket1.send(data)
    print("Sent bytes: %d" % send)

socket1.close()
sock.close()