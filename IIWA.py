from exo_net import *
from packer import *

UDP_IP = "192.169.2.1"
UDP_PORT = 10003
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.0001)
# sock.

while (True):
    package = compare_pack()
    try:
        send(package)
        data, addr = sock.recvfrom(310)
        print(data)
    except socket.timeout:
        print("Error timeout")
        continue
