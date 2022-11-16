# Program konwertujący czyste dane z MPU6050 na przyspiesznie w m/s2

file = 'polozenieZ1.txt'

sensor = []
with open("../{}".format(file), 'r') as f:
    sensor = f.read().splitlines()

for i in range(0, len(sensor)):
    sensor[i] = float(sensor[i])
    sensor[i] = (sensor[i]/16384.0) * 9.81 #m/s2

with open(file, 'w') as f:
    for line in sensor:
        f.write(f"{line}\n")
 