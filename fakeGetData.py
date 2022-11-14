#!/usr/bin/python3

import sys
import argparse
import time

# analiza argumentów wiersza poleceń 
def parser():
    p = argparse.ArgumentParser(description = 'Program pobierający wiersze ze stdin i przekazujący na stdout z zadanym interwałem.')
    p.add_argument('-d', '--delay', help = 'Liczba sekund pomiędzy wysłaniem na stdout kolejnego wiersza danych.', type = float, required = True)
     
    return p.parse_args()

p = parser()

for line in sys.stdin:                  # czytamy całą linię
    print(line, end='')  
    sys.stdout.flush()                         
    time.sleep(p.delay)

