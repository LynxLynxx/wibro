#!/usr/bin/env python3

import argparse

def parser():
    p = argparse.ArgumentParser(description='Program wyświetlający wykresy z danych otrzymanych ze strumienia wyjściowego. Użytkownik podaje ilu czyjnikom chce wyświetlić wykresy.')
    p.add_argument('-n', '--number-of-charts', help='Liczba wykresów do wyświetlenia', type=int, required=True)
    

    return p.parse_args()

p = parser()
n = p.number_of_charts

