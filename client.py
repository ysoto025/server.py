
import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
sock.settimeout(10.0)

if (len(argv) < 4) | (len(argv) > 4):
    sys.stderr.write("missing arguments or too many Arguments")
    sys.exit()

if (argv[1] == ""):
    sys.stderr.write("ERROR: empty string")
    sys.exit()
else:
    try:
        socket.gethostbyname(argv[1])
    except socket.error:
        sys.stderr.write("ERROR: wrong host")
        sys.exit()


if argv[2] == "":
    sys.stderr.write("ERROR: empty string")
    sys.exit()

if (int(argv[2]) < 0) | (int(argv[2]) > 65535):
    sys.stderr.write("ERROR: Overflow error")
    sys.exit()

try:
    sock.settimeout(10.0)
    sock.connect((argv[1], int(argv[2])))
    mess = sock.recv(5).decode("utf-8")
    if mess != "accio\r\n":
        sys.stderr.write("ERROR: no data transmitted")
    else:
        print(mess)
except socket.error:
    sys.stderr.write("ERROR: couldnt connect")
    sys.exit()
    print("File sent")

file = open(argv[3], "rb")

data = sock.recv(5).decode("utf-8")

while True:

    send = file.read(600000000)
    if len(send) < 1:
        break
    sock.send(send)

print(file)

file.close()

sock.close()