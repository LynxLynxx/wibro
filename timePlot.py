#!/usr/bin/python3

from cProfile import label
from queue import Empty
import string
import sys
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import argparse

def parser():
    p = argparse.ArgumentParser(description='Program wyświetlający wykresy z danych otrzymanych ze strumienia wyjściowego. Użytkownik podaje ile wykresów ma zostać wyświetlonych, oraz podaje ich nazwy.')
    p.add_argument('-n', '--number-of-charts', help='Liczba wykresów do wyświetlenia', type=int, required=True)
    p.add_argument('-d', '--descriptions', help='Nazwy wykresów podawane są poprzez oddzielenie ich spacjami. Nazwy nie mogą znajdować się w cudzysłowiu. Przykład: "-d x1 x2 x3"',nargs='+', required= True)
    p.add_argument('-c', '--cache', help='Liczba określająca ile elementów ma być wyświetlana w danym czasie', type=int, default=50)

    return p.parse_args()

p = parser()
n = p.number_of_charts
descriptions = tuple(p.descriptions)

if len(descriptions) != n:
    raise p.error( "Liczba podanych nazw musi zgadzać się z liczbą wykresów n")

if n < 1:
    raise p.error("Liczba wykresów nie może być mniejsza niż 1")


if n!=1:
    fig, ax = plt.subplots(n)
    fig.tight_layout(pad=3)
    fig.show()
# jeżeli rysowany będzie tylko jeden wykres
else:
    fig = plt.figure()
    ax = plt.axes() 


cacheI = 0
cache = p.cache
color = ['r', 'g', 'b']
x = []
y = []
for j in range(0,n):
    y.append([])

if n == 1:
    for line in sys.stdin:
        print(line, end='')
        l = line.split()
        l = list(map(float, l))
        if len(l) < 3:
            l = [0,0,0]

        x.append(cacheI)
        y[0].append(l[0])
        ax.plot(x,y[0], 'r')
        ax.set_title("{}".format(descriptions[0]))
        ax.set_xlabel('t[n]')

        fig.canvas.draw()
        ax.set_xlim(left=max(0, cacheI-cache), right=cacheI)

        plt.pause(0.0001)
        cacheI += 1
       
    #    todo: poprawić usuwanie danych
        # if len(y) >= cache:
        #     del y[0]

else:
    for line in sys.stdin:
        print(line, end='')
        l = line.split()
        l = list(map(float, l))
        if len(l) < 3:
            l = [0,0,0]
        # dodanie pozycji na osi x
        x.append(cacheI)
        # rysowanie punktów
        for j in range(n):
            y[j].append(l[j])
            ax[j].plot(x,y[j], 'r')
            ax[j].set_title("{}".format(descriptions[j]))
            ax[j].set_xlabel('t[n]')

        fig.canvas.draw()
        # przesuwanie wykresu w czasie
        for j in range(n):
            ax[j].set_xlim(left=max(0, cacheI-cache), right=cacheI)

        plt.pause(0.0001)
        cacheI += 1
        # todo: poprawić usuwanie danych
        # for i in range(n):
        #     if len(y[i]) >= cache:
        #         del y[i][0]
plt.close()
