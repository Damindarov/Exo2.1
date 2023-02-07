import math
import struct
import time

from exo_net import *
from packer import *
from parser import parser
import threading
import select

UDP_IP = "192.169.2.1"
UDP_PORT = 10003
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_PORT))

pr = parser()
# sock.settimeout(0.01)

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(("192.168.1.6", 8080))
print('Start_listener_server')
s1.listen(1)
conn, addr = s1.accept()

while True:
    try:
        package = compare_pack()
        send(package)
        data, addr = sock.recvfrom(310)
        L_ShoulderF = math.radians(struct.unpack('h', data[2:4])[0] * 0.085)
        pr.parse_data(data)
        print(L_ShoulderF, ' ', pr.L_ShoulderF)
        pack_to_PC = pack("ffffff", float(pr.L_ShoulderF), float(pr.L_ElbowR), float(pr.L_Elbow), float(pr.R_ShoulderF), float(-pr.R_ElbowR), float(pr.R_Elbow))
        conn.send(pack_to_PC)

    except socket.timeout:
        print("Time_error")