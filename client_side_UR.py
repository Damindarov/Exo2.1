import socket
import struct
import time
import threading
import URBasic
global time_update
time_update = time.time()

def checker():
    global time_update
    while(True):
        if time.time() - time_update > 1.1:
            print("Pizdec")
# thr2 = threading.Thread(target = thre(s),daemon=True)
# thr2.start()
# print("started")
# thr1 = threading.Thread(target = checker,daemon=True)
# thr1.start()
print("started")
# time.sleep(3)
# # thr1.start()
HOST1 = "172.31.1.25"  # The remote host
HOST2 = "172.31.1.26"  # The remote host

robotModle1 = URBasic.robotModel.RobotModel()
robotModle2 = URBasic.robotModel.RobotModel()
print("Initialization 1 UR")
#
robot2 = URBasic.urScriptExt.UrScriptExt(host=HOST2, robotModel=robotModle2)
robot2.init_realtime_control()
print("Initialization 2 UR")
robot1 = URBasic.urScriptExt.UrScriptExt(host=HOST1, robotModel=robotModle1)
robot1.init_realtime_control()
print("Initialization 1 UR")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
s.connect(('192.168.1.6', 50000))  # Подключаемся к нашему серверу.
while (True):
    try:
        #     s.sendall('Hello, Habr!'.encode('utf-8'))  # Отправляем фразу.
        # except:
        #     continue
        # print("recieve")
        s.sendall('a'.encode('utf-8'))
        data = s.recv(24)  # Получаем данные из сокета.
        # print("recieved")
        q1 = struct.unpack('f', data[0:4])[0]
        q3 = struct.unpack('f', data[4:8])[0]
        q4 = struct.unpack('f', data[8:12])[0]

        q8 = struct.unpack('f', data[12:16])[0]
        q10 = struct.unpack('f', data[16:20])[0]
        q11 = struct.unpack('f', data[20:24])[0]

        print(round(time.time(), 2), round(q1,2), round(q3,2), round(q4,2), round(q8,2), round(q10,2), round(q11,2))

        # position_arr1 = [0.0, -1.5694, 0.0, 0, 0, 0]
        # position_arr2 = [0.0, -1.5694, 0.0, 0, 0, 0]

        if -q10 < -0.6:
            q10 = 0.6
        if -q10 > 0.6:
            q10 = -0.6

        if -q3 < -0.6:
            q3 = 0.6
        if -q3 > 0.6:
            q3 = -0.6

        position_arr2 = [-q3, -q1-0.05, q4-0., -2.7,  0.0, 0]
        position_arr1 = [q10, -q8+0.05, q11+0., 0.0,  0.0, 0]
        robot1.set_realtime_pose(position_arr1)
        robot2.set_realtime_pose(position_arr2)
        # s.close()
    except ConnectionResetError as err:
        s.close()
        print("Error, server disable")
        break
    except socket.timeout:
        print("Socket timeout, check network")

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        continue
s.close()
