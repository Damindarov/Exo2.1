import math
import struct


class parser:
    init = False
    L_ShoulderF, L_Shoulder_S, L_ElbowR, L_Elbow, \
    L_WristR, L_WristS, L_WristF, L_Index, L_Little, \
    L_Middle, L_Ring, L_Thumb, R_ShoulderF, R_Shoulder_S, R_ElbowR, \
    R_Elbow, R_WristR, R_WristS, R_WristF = 0, 0, 0, 0, 0, \
                                            0, 0, 0, 0, 0, \
                                            0, 0, 0, 0, 0, \
                                            0, 0, 0, 0

    def __init__(self):
        self.init = True

    def parse_data(self, data):
        self.L_ShoulderF = math.radians(struct.unpack('h', data[2:4])[0] * 0.085)
        self.L_Shoulder_S = math.radians((struct.unpack('h', data[270:272])[0] - 2150) * 0.085)
        self.L_ElbowR = math.radians((struct.unpack('h', data[268:270])[0] - 2088) * 0.08789063)  # correct
        self.L_Elbow = math.radians(struct.unpack('h', data[34:36])[0] * -0.02)
        self.L_WristR = math.radians((-6720 - struct.unpack('h', data[18:20])[0]) * 0.085)
        self.L_WristS = math.radians(((0 - struct.unpack('h', data[264:266])[0]) + 2630) * -0.08789063)
        self.L_WristF = math.radians((2088 - struct.unpack('h', data[266:268])[0]) * 0.08789063)
        self.L_Index = math.radians((-2029 + struct.unpack('h', data[66:68])[0]) * -0.085)  # correct
        self.L_Little = math.radians((-3615 + struct.unpack('h', data[114:116])[0]) * -0.085)  # correct
        self.L_Middle = math.radians(-(1944 - struct.unpack('h', data[82:84])[0]) * 0.085)  # correct
        self.L_Ring = math.radians(-(2458 - struct.unpack('h', data[98:100])[0]) * 0.085)  # correct
        self.L_Thumb = math.radians(-(490 - struct.unpack('h', data[50:52])[0]) * 0.085)

        self.R_ShoulderF = (1600 + struct.unpack('h', data[130:132])[0]) * 0.085
        self.R_Shoulder_S = (struct.unpack('h', data[284:286])[0] - 2150) * 0.08789063  # correct
        self.R_ElbowR = (struct.unpack('h', data[278:280])[0] - 2018) * 0.08789063  # correct
        self.R_Elbow = struct.unpack('h', data[162:164])[0] * -0.02  # correct
        self.R_WristR = (-4520 - struct.unpack('h', data[146:148])[0]) * 0.085  # correct
        self.R_WristS = ((0 - struct.unpack('h', data[282:284])[0]) + 2040) * 0.08789063  # incorrect?
        self.R_WristF = ((0 - struct.unpack('h', data[280:282])[0]) + 2160) * 0.08789063
