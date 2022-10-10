#!/usr/bin/env python

import sys
import numpy as np
import argparse

# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program obliczający moduł (moduły) wektorów 3d zadanych strumieniem wejściowym. Dane w postaci trójek typu float.')
    p.add_argument('-n', '--number-of-vectors', help = 'Liczba trójek w każdym wierszu strumienia wejściowego', type = int, required = True)
    p.add_argument('-o', '--output-file', help = 'Nazwa pliku wyjściowego, równolegle zapisywanego danymi ze stdout', default = '', required = False)    
       
    return p.parse_args()


p = parser()
n = p.number_of_vectors
if (p.output_file != ''):
    f = open( p.output_file , "w")


for line in sys.stdin:                  # czytamy całą linię
    l = line.split()                   # i dzielimy ją na słowa - podział wg białych znaków, zatem i spacja i tab zadziałąją

    for i in range(0, n * 3):         # zmiana formatu - string to float
        l[i] = float(l[i])
        
    delim = ''                          # pierwszy odstęp w wierszu wyjściowym jest... nie ma odstępu - choć chyba nie zadziałało - nie wiem czemu, a nie chce mi się szukać ;)
    o = ''                              # tu będize kompletowany łańcuch wyjściowy
    for i in range(0, n):             # iteracja po trójkach liczb ze strumienia wejściowego (teraz już ze zmiennej line)
        m = np.sqrt(l[0 + i*3]**2 + l[1 + i*3]**2 + l[2 + i*3]**2)
        o = o + delim + str(m)
        #print(o, end = '')       # end='' oznacza, że nie doda teraz znaku końca wiersza
        delim = ' '                     # teraz będą odstęþy przed każdą kolejną liczbą w wierszu
        
    print(o) 
    if (p.output_file != ''):
        print(o, file=f)              
        f.flush()
    sys.stdout.flush()                  # potrzebne, jeśłi działamu na strumieniach i pipach - inaczej czeka aż się proces skończy i wtedy opróżnia bufor


