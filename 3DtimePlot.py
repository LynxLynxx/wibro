#!/usr/bin/python3
import sys
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import argparse
from mpl_toolkits import mplot3d

# TODO: argparser
#* despription
#* cache

def parser():
    p = argparse.ArgumentParser(description='Program wyświetla dane, które otrzyma w przestrzeni 3D ')
    p.add_argument('-c', '--cache', help='Liczba określająca ile punktów ma być wyświetlane na wykresie w danym czasie', required=True, type=int)
    p.add_argument('-d', '--description', help='Nazwa wykresu', required= True, nargs='+')

    return p.parse_args()

def on_close(event):
    print('Closed Figure!')
    sys.exit()

p = parser()
description = tuple(p.description)
cache = p.cache
cacheI = 0
if cache < 1:
    raise p.error("Liczba nie może być mniejsza niż 1")


fig = plt.figure()
ax = plt.axes(projection='3d')
fig.canvas.mpl_connect('close_event', on_close)

x,y,z = [], [], []

# TODO: wyświetlanie danych w 3D na jednym wykresie
for line in sys.stdin:
    # print(line, end='')
    l = line.split()
    l = list(map(float,l))
    if len(l) < 3:
        l = [0,0,0]

    x.append(l[0])
    y.append(l[1])
    z.append(l[2])

    ax.scatter3D(x,y,z, color='red')
    ax.set_title(" ".join(description))

    fig.canvas.draw()

    plt.pause(0.001)
    if len(x) >= cache:
        del x[0]
        del y[0]
        del z[0]
    
    plt.cla()
    fig.canvas.flush_events()

plt.close()