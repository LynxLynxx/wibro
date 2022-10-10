#!/usr/bin/env python

import sys
import numpy as np
import argparse

# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program obliczający współczynnik korelacji wzajemnej (Pearsona) dla dwóch przebiegów w zakresie zadanej długości ciągu.')
    p.add_argument('-n', '--number-of-points', help = 'Długość ciągu czasowego (liczba punktów pomiarowych) do obliczenia korelacji.', type = int, required = True)
    p.add_argument('-o', '--output-file', help = 'Nazwa pliku wyjściowego, równolegle zapisywanego danymi ze stdout', default = '', required = False)  

    return p.parse_args()


p = parser()
n = p.number_of_points

#x1, x2 = [], []

for i in range (0, n):
    x1.append(0)
    x2.append(0)

if (p.output_file != ''):
    f = open( p.output_file , "w")

for line in sys.stdin:                  # czytamy całą linię
    l = line.split()                   # i dzielimy ją na słowa - podział wg białych znaków, zatem i spacja i tab zadziałąją

    x1.append(float(l[0]))                 # tylko dwie kolumny. Jeśłi jest więcej kolumn, to pozostałe są ignorowane
    x2.append(float(l[1]))

    del x1[0]
    del x2[0]
        
    o = str( np.corrcoef(x1 ,x2)[0, 1] ) 
        
    print(o) 
    if (p.output_file != ''):
        print(o, file=f)              
        f.flush()
    sys.stdout.flush()                  # potrzebne, jeśli działamy na strumieniach i pipach - inaczej czeka aż się proces skończy i wtedy opróżnia bufor


