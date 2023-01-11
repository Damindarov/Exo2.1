import socket
import numpy as np
import time
from struct import *
import struct
import math
import threading

global time_update
global sock
time_update = time.time()


def checker():
    global sock
    global time_update
    while (True):
        if time.time() - time_update > 0.2:
            try:
                print("Pack")
                # sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
                pa = pack(
                    'bbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhh',
                    1, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # плечо левая
                    2, MODE, int(Us), TORQUE, CENTER, STIFF, enable, int(Val_maxs), int(Val_maxs),  # кисть
                    3, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # локоть
                    4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(490 + 60 / 0.085), int(490 + 20 / 0.085),  # большой
                    5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(2029 + 60 / 0.085), int(2029 + 70 / 0.085),
                    # указательный
                    6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(1934 + 0 / -0.085), int(1934 + 60 / -0.085),
                    # средний
                    7, MODE, 456, 3000, CENTER, STIFF, 0, int(3000), int(3000),
                    # int((2478 + 60/0.085)),int(2478 + 10/0.085),#безымянный()
                    8, MODE, ANGLE, 3000, CENTER, STIFF, 0, 3000, 3200,  # мизинец()

                    1, MODE, int(Us_Shoulder), TORQUE, CENTER, STIFF, enable_Shoulder, int(Val_maxs_Shoulder),
                    int(Val_mins_Shoulder),  # правая
                    2, MODE, int(Us1), TORQUE, CENTER, STIFF, enable1, int(Val_maxs1), int(Val_mins1),
                    3, MODE, int(Us_Elbow), TORQUE, CENTER, STIFF, enable_Elbow, int(Val_maxs_ELbow),
                    int(Val_mins_ELbow),
                    4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                    5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                    6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                    7, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                    8, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, 1616 + 550, 1616 + 700)
                print("Send")
                send(pa)

                data, addr = sock.recvfrom(310)
                print("recieve")

                sock.shutdown(1)
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.bind((UDP_IP, UDP_PORT))

                # pa = pack(
                # 'bbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhh',
                # 1, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # плечо левая
                # 2, MODE, int(Us), TORQUE, CENTER, STIFF, enable, int(Val_maxs), int(Val_maxs),  # кисть
                # 3, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # локоть
                # 4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(490 + 60 / 0.085), int(490 + 20 / 0.085),  # большой
                # 5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(2029 + 60 / 0.085), int(2029 + 70 / 0.085),  # указательный
                # 6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(1934 + 0 / -0.085), int(1934 + 60 / -0.085),  # средний
                # 7, MODE, 456, 3000, CENTER, STIFF, 0, int(3000), int(3000),
                # # int((2478 + 60/0.085)),int(2478 + 10/0.085),#безымянный()
                # 8, MODE, ANGLE, 3000, CENTER, STIFF, 0, 3000, 3200,  # мизинец()

                # 1, MODE, int(Us_Shoulder), TORQUE, CENTER, STIFF, enable_Shoulder, int(Val_maxs_Shoulder),
                # int(Val_mins_Shoulder),  # правая
                # 2, MODE, int(Us1), TORQUE, CENTER, STIFF, enable1, int(Val_maxs1), int(Val_mins1),
                # 3, MODE, int(Us_Elbow), TORQUE, CENTER, STIFF, enable_Elbow, int(Val_maxs_ELbow), int(Val_mins_ELbow),
                # 4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                # 5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                # 6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                # 7, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                # 8, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, 1616 + 550, 1616 + 700)

                # send(pa)

                # data, addr = sock.recvfrom(310)
                print("Pizdec")
            except Exception as a:
                time_update = time.time()
                print("Polniy pizdec", a)


def send(data, port=10003, addr='192.169.2.15'):
    """send(data[, port[, addr]]) - multicasts a UDP datagram."""
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Make the socket multicast-aware, and set TTL.
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20)  # Change TTL (=20) to suit
    # Send the data
    s.sendto(data, (addr, port))


def recv(port=10003, addr="192.169.2.15", buf_size=310):
    """recv([port[, addr[,buf_size]]]) - waits for a datagram and returns the data."""
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set some options to make it multicast-friendly
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    except AttributeError:
        pass  # Some systems don't support SO_REUSEPORT
    s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
    s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)

    # Bind to the port
    s.bind(('', port))

    # Set some more multicast options
    intf = socket.gethostbyname(socket.gethostname())
    s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(intf))
    s.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(addr) + socket.inet_aton(intf))

    # Receive the data, then unregister multicast receive membership, then close the port
    data, sender_addr = s.recvfrom(buf_size)
    s.setsockopt(socket.SOL_IP, socket.IP_DROP_MEMBERSHIP, socket.inet_aton(addr) + socket.inet_aton('0.0.0.0'))
    s.close()
    return data


UDP_IP = "192.169.2.1"
UDP_PORT = 10003
global sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))
a1, a2, a3, a4 = 0.08, 0.42, 0.4, 0.126
pi = np.pi
# time.sleep(1)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s1.bind(("192.168.1.6", 3030))  # Привязываем серверный сокет к localhost и 3030 порту.
# s1.listen(1)  # Начинаем прослушивать входящие соединения.
# conn, addr = s1.accept()  # Метод который принимает входящее соединение.


UDP_IP = "192.169.2.1"
UDP_PORT = 10003
MODE = 0
ANGLE = -700
TORQUE = 0
CENTER = 0
STIFF = 0
DUMP = 0
POSMIN = 0
POSMAX = 0
Us = 0
Val_mins = 0
Val_maxs = 0
enable = 0

Us1 = 0
Val_mins1 = 0
Val_maxs1 = 0
enable1 = 0

Us_Elbow = 0
Val_mins_ELbow = 0
Val_maxs_ELbow = 0
enable_Elbow = 0

Us_Shoulder = 0
Val_mins_Shoulder = 0
Val_maxs_Shoulder = 0

a1, a2, a3, a4 = 0.08, 0.42, 0.4, 0.126
pi = np.pi
deltaR_val = -5682
deltaL_val = -6720
delta_R_Shoulder_val = 0
time_start = time.time()
time_change = time.time()
enable_Shoulder = 0
prev_t = 0
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

thr1 = threading.Thread(target=checker)
thr1.start()
print("I started")

while (True):
    # print(time.time() - prev_t)
    # all this values in angels
    try:
        prev_t = time.time()
        frame = []
        # print("send")
        time_update = time.time()
        # print("I Packed")
        pa = pack(
            'bbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhh',
            1, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # плечо левая
            2, MODE, int(Us), TORQUE, CENTER, STIFF, enable, int(Val_maxs), int(Val_maxs),  # кисть
            3, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # локоть
            4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(490 + 60 / 0.085), int(490 + 20 / 0.085),  # большой
            5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(2029 + 60 / 0.085), int(2029 + 70 / 0.085),  # указательный
            6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(1934 + 0 / -0.085), int(1934 + 60 / -0.085),  # средний
            7, MODE, 456, 3000, CENTER, STIFF, 0, int(3000), int(3000),
            # int((2478 + 60/0.085)),int(2478 + 10/0.085),#безымянный()
            8, MODE, ANGLE, 3000, CENTER, STIFF, 0, 3000, 3200,  # мизинец()

            1, MODE, int(Us_Shoulder), TORQUE, CENTER, STIFF, enable_Shoulder, int(Val_maxs_Shoulder),
            int(Val_mins_Shoulder),  # правая
            2, MODE, int(Us1), TORQUE, CENTER, STIFF, enable1, int(Val_maxs1), int(Val_mins1),
            3, MODE, int(Us_Elbow), TORQUE, CENTER, STIFF, enable_Elbow, int(Val_maxs_ELbow), int(Val_mins_ELbow),
            4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
            5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
            6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
            7, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
            8, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, 1616 + 550, 1616 + 700)

        send(pa)

        data, addr = sock.recvfrom(310)
        # sock.close()

        L_ShoulderF = struct.unpack('h', data[2:4])[0] * 0.085  # incorrect?
        L_Shoulder_S = (struct.unpack('h', data[270:272])[0] - 2150) * 0.08789063  # correct
        L_ElbowR = (struct.unpack('h', data[268:270])[0] - 2088) * 0.08789063  # correct
        L_Elbow = struct.unpack('h', data[34:36])[0] * -0.02  # correct
        L_WristR = (deltaL_val - struct.unpack('h', data[18:20])[0]) * 0.085  # correct
        L_WristS = ((0 - struct.unpack('h', data[264:266])[0]) + 2630) * -0.08789063  # incorrect?
        L_WristF = ((2088 - struct.unpack('h', data[266:268])[0])) * 0.08789063
        # block for fingers
        L_Index = (-2029 + struct.unpack('h', data[66:68])[0]) * -0.085  # correct
        L_Little = (-3615 + struct.unpack('h', data[114:116])[0]) * -0.085  # correct
        L_Middle = -(1944 - struct.unpack('h', data[82:84])[0]) * 0.085  # correct
        L_Ring = -(2458 - struct.unpack('h', data[98:100])[0]) * 0.085  # correct
        L_Thumb = -(490 - struct.unpack('h', data[50:52])[0]) * 0.085

        R_ShoulderF = (-delta_R_Shoulder_val + struct.unpack('h', data[130:132])[0]) * 0.085
        R_Shoulder_S = (struct.unpack('h', data[284:286])[0] - 2150) * 0.08789063  # correct
        R_ElbowR = (struct.unpack('h', data[278:280])[0] - 2018) * 0.08789063  # correct
        R_Elbow = struct.unpack('h', data[162:164])[0] * -0.02  # correct
        R_WristR = (deltaR_val - struct.unpack('h', data[146:148])[0]) * 0.085  # correct
        R_WristS = ((0 - struct.unpack('h', data[282:284])[0]) + 2040) * 0.08789063  # incorrect?
        R_WristF = ((0 - struct.unpack('h', data[280:282])[0]) + 2160) * 0.08789063

        R_Index = (-2692 + struct.unpack('h', data[194:196])[0]) * -0.085
        q3 = 0

        q1, q2, q3, q4, q5, q6, q7 = math.radians(L_ShoulderF), math.radians(L_Shoulder_S), math.radians(
            L_ElbowR), math.radians(L_Elbow), math.radians(L_WristR), math.radians(L_WristS), math.radians(L_WristF)
        q8, q9, q10, q11, q12, q13 = math.radians(R_ShoulderF), math.radians(R_Shoulder_S), math.radians(R_ElbowR), \
                                     math.radians(R_Elbow), math.radians(R_WristR), math.radians(
            R_WristS)

        # print(round(T45[0, -1], 2)+0.4, round(T45[1, -1], 2)+0.27, round(T45[2, -1], 2)-0.3)
        position_arr1 = [0.0, -1.5694, 0.0, 0, 0, 0]
        position_arr2 = [0.0, -1.5694, 0.0, 0, 0, 0]
        if q11 < 0.44:
            q11 = 0.44
        if q4 > -0.44:
            q4 = -0.44

        if -q10 < -0.14:
            q10 = 0.14
        if -q10 > 0.14:
            q10 = -0.14

        if -q3 < -0.14:
            q3 = 0.14
        if -q3 > 0.14:
            q3 = -0.14

        pack_to_PC = pack("ffffff", q1, q3, q4, q8, -q10, q11)
        # conn.sendall(pack_to_PC)
    # print("")
        print("left: ", q1, q3, q4, "right: ",q8, -q10, q11)
    except:
        print("Error\n\n\n\n\n")

