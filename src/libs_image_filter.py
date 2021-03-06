from PIL import Image, ImageTk
import numpy as np
from libs_image_filter import *

import os


def filter_pixel(_path):
    data = np.asarray(Image.open(_path)).copy()
    print(type(data))
    print(data.shape)
    print(data[0][0][0])

    step = 30

    for I in range(0, int(len(data)/step)):
        for K in range(0, int(len(data[0])/step)):
            color = average_color(data, I*step, K*step, step)

            for L in range(I * step, I * step + step):
                for M in range(K * step, K * step + step):
                    data[L][M] = color

    Image.fromarray(data).save("filtered-tiger", "JPEG")


def average_color(_data, _y, _x, s):
    color = [0, 0, 0]

    for I in range(s * int(_y/s), s + s * int(_y/s)):
        for K in range(s * int(_x/s), s + s * int(_x/s)):
            color[0] += _data[I][K][0]
            color[1] += _data[I][K][1]
            color[2] += _data[I][K][2]

    color[0] = int(color[0]/(s*s))
    color[1] = int(color[1]/(s*s))
    color[2] = int(color[2]/(s*s))
    return color


def average_grayscale(_data, _y, _x, s):
    color = [0, 0]

    for I in range(s * int(_y/s), s + s * int(_y/s)):
        for K in range(s * int(_x/s), s + s * int(_x/s)):
            color[0] += _data[I][K][0]
            color[1] += _data[I][K][1]

    color[0] = int(color[0]/(s*s))
    color[1] = int(color[1]/(s*s))
    return color


def filter_ascii(_path, _y, _x):
    data = np.asarray(Image.open(_path).resize((_y, _x)).convert('LA')).copy()
    print(type(data))
    print(data.shape)
    print(data[0][0][0])

    step = 10
    line_count = 0

    for I in range(0, int(_y/step)):
        for K in range(0, int(_x/step)):
            color = average_grayscale(data, I*step, K*step, step)

            chr_l = [
                "8", "#", "m",
                "m", "v", "=",
                "*", "+", "º",
                "1",  "\\", "/",
                ":", "\"", "-",
                "'", ",", ".",
                "_", " ", " "
            ]
            with open("./ascii.txt", 'a') as f:
                print(chr_l[int(color[0]/13)] + "  ", end='')
                f.write(chr_l[int(color[0]/13)] + "  ")
                line_count += 1

                if(line_count == int(_x/10)):
                    print()
                    f.write("\n")
                    line_count = 0
