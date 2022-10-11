#!/usr/bin/python3

import sys
import numpy as np
import argparse

# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program zamieniający notację hex na dec. liczba danych do konwersji (liczba kanałów) rozpoznawana automatycznie na podstawie długości łańcucha wejściowego.')
    p.add_argument('-o', '--output-file', help = 'Nazwa pliku wyjściowego, równolegle zapisywanego danymi ze stdout', default = '', required = False)    
    
    return p.parse_args()

p = parser()
if (p.output_file != ''):
    f = open( p.output_file , "w")
    
for line in sys.stdin:
    pos = 0
    delim = ''
#    print (line)

    o = ''
    while (pos+4 < len(line)):
        num = line[pos: pos+4]
#        print (num)
        x = np.int16(int(num,16))
        o = o + delim + str(x)
        delim = ' '
        pos = pos + 4
        
    print(o) 
    if (p.output_file != ''):
        print(o, file=f)              
        f.flush()
    sys.stdout.flush()                  # potrzebne, jeśli działamy na strumieniach i pipach - inaczej czeka aż się proces skończy i wtedy opróżnia bufor

