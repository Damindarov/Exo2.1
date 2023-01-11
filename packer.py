from struct import *
from base_parameters import *


def compare_pack():
    pa = pack(
                'bbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhhbbhhhhhhh',
                1, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # плечо левая
                2, MODE, int(Us), TORQUE, CENTER, STIFF, 0, int(Val_maxs), int(Val_maxs),  # кисть
                3, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # локоть
                4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(490 + 60 / 0.085), int(490 + 20 / 0.085),  # большой
                5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(2029 + 60 / 0.085), int(2029 + 70 / 0.085),  # указательный
                6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, int(1934 + 0 / -0.085), int(1934 + 60 / -0.085),  # средний
                7, MODE, 456, 3000, CENTER, STIFF, 0, int(3000), int(3000),
                # int((2478 + 60/0.085)),int(2478 + 10/0.085),#безымянный()
                8, MODE, ANGLE, 3000, CENTER, STIFF, 0, 3000, 3200,  # мизинец()

                1, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,  # правая
                2, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                3, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                4, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                5, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                6, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                7, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX,
                8, MODE, ANGLE, TORQUE, CENTER, STIFF, 0, POSMIN, POSMAX)
    return pa