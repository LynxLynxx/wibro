#!/usr/bin/env python3

from cProfile import label
from queue import Empty
import string
import sys
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time
from datetime import datetime
import argparse

def parser():
    p = argparse.ArgumentParser(description='Program wyświetlający wykresy z danych otrzymanych ze strumienia wyjściowego. Użytkownik podaje ile wykresów ma zostać wyświetlonych, oraz podaje ich nazwy.')
    p.add_argument('-n', '--number-of-charts', help='Liczba wykresów do wyświetlenia', type=int, required=True)
    p.add_argument('-d', '--descriptions', help='Nazwy wykresów podawane są poprzez oddzielenie ich spacjami. Nazwy nie mogą znajdować się w cudzysłowiu. Przykład: "-d x1 x2 x3"',nargs='+', required= True)

    return p.parse_args()

p = parser()
n = p.number_of_charts
descriptions = tuple(p.descriptions)

print(descriptions)

fig, ax = plt.subplots(3)
print("Start 2")
fig.show()

print("Start 3")

i = 0
cache = 100
x,y1, y2, y3 = [], [], [], []

#while 1:
#    line = sys.stdin.readline()
for line in sys.stdin:
    print(line, end='')
    l = line.split()
    l = list(map(float, l))
    if len(l) < 3:
        l = [0,0,0]
    
#    if l[2] < 10000:
#        l[2] = 10000

    x.append(i)
    y1.append(l[0])
    y2.append(l[1])
    y3.append(l[2])

    ax[0].plot(x,y1, 'r', )
    ax[0].set_title("x")

    ax[1].plot(x,y2, 'g', )
    ax[1].set_title("y")


    ax[2].plot(x,y3, 'y', )
    ax[2].set_title("z")
    # ax.legend(['x', 'y', 'z'])

    fig.canvas.draw()

    ax[0].set_xlim(left=max(0, i-cache), right=i+cache)
    ax[1].set_xlim(left=max(0, i-cache), right=i+cache)
    ax[2].set_xlim(left=max(0, i-cache), right=i+cache)
    #plt.pause(0.0001)
    i += 1

plt.close()
