#!/usr/bin/env python3

from cProfile import label
from queue import Empty
import string
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
import argparse
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

def parser():
    p = argparse.ArgumentParser(description='Program wyświetlający wykresy FFT z danych otrzymanych ze strumienia wyjściowego. Wykresy modułu i fazy przedstawiają wartości chwilowe. Wykres 3d przedstawia przebieg zmienności wartości modułu w czasie')
    p.add_argument('-n', '--number-of-points', help='Liczba punktów czasowych do wyświetlenia danych na wykresie 3d.', type=int, required=True)

    return p.parse_args()

def on_close(event):
    print('Closed Figure!')
    sys.exit()

def plot2din3d(x,y,z):
    ax2.plot(x, y, zs=z, zdir='z')
    ColObj= ax2.fill_between(x, 0.5, y, step='pre', alpha=0.1) 
    ax2.add_collection3d(ColObj, zs = z, zdir = 'z')

p = parser()
n = p.number_of_points

x = []
for i in range(0, n):
    x.append([])


# tutaj sobie zainicjalizuj wykresy itp
fig = plt.figure(figsize=(16,9))
ax0 = fig.add_subplot(2,2,1)
ax1 = fig.add_subplot(2,2,3)
ax2 = fig.add_subplot(2,2,(2,4), projection='3d')
ax2.view_init(30, -100)
fig.tight_layout(pad=3)
fig.canvas.mpl_connect('close_event', on_close)





first = 1
cacheI = 0
for line in sys.stdin:
    # print(line, end='')
    l = line.split()
    l = list(map(float, l))
    
# to ma się wykonać tylko raz, w celu zainicjowania tablicy x
# wcześniej nie wiadomo było jaka ma być duża, a teraz po pdczytaniu linii wiadomo ile w niej jest danych  
    if(first):
        fig.show()

        first = 0
        x = []
        yAxis = []
        for i in range(0, n):
            x.append([]) 
            for j in range(0, int(len(l)/2)):
                x[i].append(0)
      
# w liście x będziesz miał teraz same puste (z zerami) n list do wykresu 3d
# tym sposobem wykres nie będize się poszerzał, tylko na starcie będzie taki szeroki jaki ma myć - tylko dane będą napływały i wypierały zera
# swoją drogą, może w timePlotach zrób tak samo i zniknie problem wywalania błędów przy manipulacjach z kolejką?
    modulus = []
    angle = []    

    for i in range(0,len(l), 2):
        z = complex(l[i], l[i+1])
        modulus.append(np.absolute(z))
        angle.append(np.angle(z))
         
    x.append(modulus)           #dodaj nowy wektor z modułami na końcu listy
    del x[0]                    #i usuń nadmiarowy z początku

    

    
    yAxis.append(cacheI)
    
    # teraz masz:
    # w modulus i angle - dane dla wykresów 2d z wartościami chwilowymi
    # w x - historyczne dane modulus do wykresu 3d
    # print(modulus)
   
    xAxis1 = np.linspace(0, 0.5, len(modulus))
    xAxis2 = np.linspace(0, 0.5, len(angle))
    ax0.plot(xAxis1, modulus, 'r')
    ax0.set_title("Moduł")
    ax0.set_xlabel('f[fs]')
    ax1.plot(xAxis2,angle, 'g')
    ax1.set_title("Faza")
    ax1.set_xlabel('f[fs]')

    ax2.set_title("Moduł w czasie")

    ax2.plot(xAxis1, modulus, yAxis[-1], cmap = cm.coolwarm)
    ax2.set_xlabel("x")
    ax2.set_ylabel('y')

    fig.canvas.draw()

    plt.pause(0.0001)
    ax0.clear()
    ax1.clear()
    # ax2.clear()


    cacheI += 1
plt.close()
    
 
