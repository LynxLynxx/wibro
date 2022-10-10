#!/usr/bin/env python

import sys
import numpy as np
import argparse

# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program obliczający wypadkową wartość pomiędzy dwoma punktami. Pierwszy punkt domyśnie na współrzędnych (0,0,0), drugi zadany parametrami. Dane z obu czujników domyślnie zorientowane jednakowo względem kartezjańskiego układu współrzędnych. Program umożliwia interpolację pomiędzy punktami, a także ekstrapolację poza nie. Dane w postaci dwóch trójek typu float.')
    p.add_argument('-x', '--x', help = 'Współrzędna x drugiego punktu', type = float, required = True)
    p.add_argument('-y', '--y', help = 'Współrzędna y drugiego punktu', type = float, required = True)
    p.add_argument('-z', '--z', help = 'Współrzędna z drugiego punktu', type = float, required = True)
    p.add_argument('-t', '--t', help = 'Położenie punktu interpolowanego/ekstrapolowanego. Wartość 0 - położenie w punkcie 1, 1 - położenie w punkcie 2, wartości pomiędzy 0 i 1 - położenie na prostej łączącej punkty 1 i 2, pomiędzy nimi. Wartości mniejsze od 0 i większe od 1 ekstrapolują wartości poza odcinkiem 1-2.', type = float, required = True)
    p.add_argument('-o', '--output-file', help = 'Nazwa pliku wyjściowego, równolegle zapisywanego danymi ze stdout', default = '', required = False)    
       
    return p.parse_args()


p = parser()
if (p.output_file != ''):
    f = open( p.output_file , "w")


for line in sys.stdin:                  # czytamy całą linię
    l = line.split()                   # i dzielimy ją na słowa - podział wg białych znaków, zatem i spacja i tab zadziałąją
    l = list(map(float, l))

    x = l[0] + p.t*(l[3]-l[0])
    y = l[1] + p.t*(l[4]-l[1])
    z = l[2] + p.t*(l[5]-l[2])
        
    o = str(x) + ' ' + str(y) + ' ' + str(z)                              # tu będzie kompletowany łańcuch wyjściowy
        
    print(o) 
    if (p.output_file != ''):
        print(o, file=f)              
        f.flush()
    sys.stdout.flush()                  # potrzebne, jeśli działamy na strumieniach i pipach - inaczej czeka aż się proces skończy i wtedy opróżnia bufor


