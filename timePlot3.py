#!/usr/bin/python3

import argparse
from functools import cache
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
import sys

def parser():
    p = argparse.ArgumentParser(description='Program wyświetlający wykresy z danych otrzymanych ze strumienia wyjściowego. Użytkownik podaje ilu czyjnikom chce wyświetlić wykresy.')
    p.add_argument('-n', '--number-of-subplots', help='Liczba danych do wyświetlenia na jednym subplocie', type=int, required=True)
    p.add_argument('-d', '--descriptions', help='Nazwy wykresów podawane w odstępie poprzez spacje. Przykład: -d x y z', required=True, nargs='+')
    p.add_argument('-c', '--cache', help='Liczba określająca ile elementów ma być wyświetlana w danym czasie', type=int, default=50)
       

    return p.parse_args()

p = parser()
n = p.number_of_subplots
descriptions = tuple(p.descriptions)

if len(descriptions) != 3:
    raise p.error("Należy podać 3 nazwy dla wykresów")

if n < 1:
    raise p.error("Liczba danych dla subplotu nie może być mniejsza niż 1")


fig, ax = plt.subplots(3)
fig.tight_layout(pad=3)
fig.show()


cacheI = 0
cache = p.cache

x = []
# stworzenie tablic dla każdego subplotu
y = [[], [], []]
color = ['r', 'g', 'b', 'y']
labels = ["Czujnik 1", "Czujnik 2", "Czujnik 3", "Czujnik 4"]

for subplot in range(3):
    for i in range(n):
        y[subplot].append([])

for line in sys.stdin:
    # print(line, end='')
    l = line.split()
    l = list(map(float, l))
    l = l[0:n*3]
    print("Otrzymano {}".format(l))
    # zabezpieczenie gdyby przyszła nie pełna paczka
    if len(l) < 3:
        l = [0,0,0]

    # dodanie pozycji dla osi x
    x.append(cacheI)
    
    # rysowanie dla każdego subplotu wykresów
    for j in range(3):
        # rysowanie n wykresów dla subplotu

        osie = l[j::3]
        for i in range(len(osie)):
            y[j][i].append(osie[i])

    for i in range(3):
        for j in range(n):
            ax[i].plot(x,y[i][j], color[j], label=labels[j])
            ax[i].set_title("{}".format(descriptions[i]))
            ax[i].set_xlabel('t[n]')
    
    
    # lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    # lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    # fig.legend(lines, labels)
    # fig.legend().set_visible(False)

    fig.canvas.draw()
    for jj in range(3):
        ax[jj].set_xlim(left=max(0, cacheI-cache), right=cacheI)
    plt.pause(0.0001)
    cacheI +=1
    fig.canvas.flush_events()

plt.close()



