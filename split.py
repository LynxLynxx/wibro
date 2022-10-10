#!/usr/bin/env python

import sys
import numpy as np
import argparse

# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program prezkazujący dane ze stdin na stdout oraz do wskazanego parametrem pliku.')
    p.add_argument('-o', '--output-file', help = 'Nazwa pliku wyjściowego, równolegle zapisywanego danymi ze stdout', default = '', required = False)    
       
    return p.parse_args()


p = parser()
f = open( p.output_file , "w")

for line in sys.stdin:                  # czytamy całą linię
    print(line, end='') 
    print(line, file=f, end='')              
    f.flush()
    sys.stdout.flush()                  # potrzebne, jeśłi działamu na strumieniach i pipach - inaczej czeka aż się proces skończy i wtedy opróżnia bufor


