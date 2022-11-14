#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

polozenieZ = []
sensorZ = []

with open("polozenieZ1.txt", "r") as f:
    polozenieZ = f.read().splitlines()

for i in range(0, len(polozenieZ)):
    polozenieZ[i] = float(polozenieZ[i])

with open("akselerometrZ1.txt", "r") as f:
    sensorZ = f.read().splitlines()

for i in range(0, len(sensorZ)):
    sensorZ[i] = float(sensorZ[i])

print(type(polozenieZ[1]))
fftPolozenie = np.abs(np.fft.fft(polozenieZ))
fftSensor = np.abs(np.fft.fft(sensorZ))
fftPolozenie = fftPolozenie[1:len(fftPolozenie/2)]
fftSensor = fftSensor[1:len(fftSensor/2)]

xAxis = np.linspace(0,0.5, len(fftPolozenie))
plt.figure(0, figsize=(25,10))
plt.plot(xAxis, fftPolozenie, label = "Czujnik położenia")
plt.plot(xAxis,fftSensor, label = "Akcelerometr")
plt.xlabel("f[fs]")

plt.legend()


plt.show()
plt.savefig("fft1.png", dpi=300, bbox_inches='tight')