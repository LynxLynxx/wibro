#!/usr/bin/python3

import sys
import numpy as np
import argparse


# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program obliczający cyklicznie rzeczywistą transformatę fouriera w formule moduł-faza, na podstawie ciągu wejściowego o zadanej długości z zadanym przeskokiem. Dla N elementów wejściowych zwraca N+2 elementów parami [Realis Imaginaris], tj. N/2+1 par')
    p.add_argument('-n', '--number-of-points', help = 'Długość ciągu czasowego (liczba punktów pomiarowych) do obliczenia rfft.', type = int, required = True)
    p.add_argument('-f', '--offset', help = 'Przeskok - co tyle punktów obliczane będize kolejne rfft.', type = int, required = True)
    p.add_argument('-o', '--output-file', help = 'Nazwa pliku wyjściowego, równolegle zapisywanego danymi ze stdout', default = '', required = False)  

    return p.parse_args()


p = parser()
n = p.number_of_points

x = []

for i in range (0, n):
    x.append(0)


if (p.output_file != ''):
    f = open( p.output_file , "w")

offset = p.offset                   #licznik przeskoku
for line in sys.stdin:                  # czytamy całą linię
    l = line.split()                   # i dzielimy ją na słowa - podział wg białych znaków, zatem i spacja i tab zadziałąją

    x.append(float(l[0]))                 # tylko jedna kolumna. Jeśłi jest więcej kolumn, to pozostałe są ignorowane
    del x[0]
  
    offset = offset - 1
    if (offset == 0):
        offset = p.offset
        f = np.fft.rfft(x)
        
        o = ''
        for q in f:
            o = o + str(q.real) + " " + str(q.imag) + " "
        
        # print("1")
        print(o)
        if (p.output_file != ''):
            print(o, file=f)              
            f.flush()
        sys.stdout.flush()                  # potrzebne, jeśli działamy na strumieniach i pipach - inaczej czeka aż się proces skończy i wtedy opróżnia bufor


