from exo_net import *
from packer import *
from parser import parser
import threading
import select
def server(pr):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s1.bind(("192.168.1.6", 8080))
    s1.listen(1)


    # s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s1.bind(("192.168.1.6", 8080))  # Привязываем серверный сокет к localhost и 3030 порту.
    # s1.listen(1)
    conn, addr = s1.accept()  # Метод который принимает входящее соединение.
    # ass = conn.recvfrom(12)
    # s1.settimeout(0.01)
    print("accept")
    while True:
        # conn.setblocking(0)
        try:
            if pr.R_Elbow < 0.44:
                pr.R_Elbow = 0.44

            if pr.L_Elbow > -0.44:
                pr.L_Elbow = -0.44

            if -pr.R_ElbowR < -0.14:
                pr.R_ElbowR = 0.14
            if -pr.R_ElbowR > 0.14:
                pr.R_ElbowR = -0.14

            if -pr.L_ElbowR < -0.14:
                pr.L_ElbowR = 0.14
            if -pr.L_ElbowR > 0.14:
                pr.L_ElbowR = -0.14
            # print(conn)
            pack_to_PC = pack("ffffff", pr.L_ShoulderF, pr.L_ElbowR, pr.L_Elbow, pr.R_ShoulderF, -pr.R_ElbowR, pr.R_Elbow)
            conn.sendall(pack_to_PC)
        except:
            print("Error")

UDP_IP = "192.169.2.1"
UDP_PORT = 10003
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
# sock.settimeout(0.01)
pr = parser()
error_couter = 0
thr1 = threading.Thread(target=server, args=(pr,))
thr1.start()

while True:
    package = compare_pack()
    try:
        send(package)
        data, addr = sock.recvfrom(310)
        pr.parse_data(data)
        # print(pr.L_ShoulderF, ' ', error_couter)
    except socket.timeout:
        print("Error timeout")
        error_couter += 1
        continue