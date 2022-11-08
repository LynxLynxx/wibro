#!/usr/bin/python3

import readline
import serial
import argparse
import numpy as np
import sys

parser = argparse.ArgumentParser(description="Czujnik drgań")
parser.add_argument('-p', '--port', type=str, help="Port, z którego czytane będą dane pomiarowe.", required=True)
parser.add_argument('-b', '--baud-rate', type=int, help="Szybkść bitowa dla portu szeregowego.", required=False, default=115200)
parser.add_argument('-o', '--output-filename', type=str, help="Nazwa pliku, w którym będą zapisywane dane. Jeśli nie podano, dane są przekazywane jedynie na stdout.", default='')
parser.add_argument('-n', '--number-of-sensors', type=int, help="Liczba kanłów (czujników) w strumieniu wejściowym.", required=False, default=1)
args = parser.parse_args()

if args.number_of_sensors == 4 or args.number_of_sensors == 2 or args.number_of_sensors == 1:
    pass
else:
    raise Exception("Podano złą liczbę kanałów - dopuszczalne wartości to 1, 2 lub 4")

fileName = args.output_filename
portName = args.port
baudRate = args.baud_rate

serialConn = serial.Serial(portName, baudRate, timeout=4)
# serialConn = serial.Serial("/dev/ttyUSB0", 115200, timeout=4)

if (fileName != ''):
    f = open( fileName, "w")

while 1:
    rawData = serialConn.readline()
    rawData = rawData.decode("utf-8")
    print(rawData)
    if (fileName != ''):
        print(rawData, file=f) 
        f.flush()             
    pos = 0
    convertData = []
    while pos + 4 < len(rawData):
        x = np.int16(int(rawData[pos: pos + 4], 16))
        convertData.append(x)
        pos = pos + 4

    print(" ".join(str(e) for e in convertData))
    sys.stdout.flush()

