import gc
gc.collect()

import adafruit_mpu6050
import board
import TM1637
from time import sleep, localtime
from math import trunc

CLK = board.D8
DIO = board.D7
print('Creating display')
display = TM1637.TM1637(CLK, DIO)
G = 9.81

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

debug = False

max_data_points = 10
glist = []

while True:
    (xa, ya, za) = mpu.acceleration
    xg = xa / G
    yg = ya / G
    zg = za / G
    totalg = (xg**2 + yg**2 + zg**2)**0.5 - 1 #
    glist.append(totalg)
    if len(glist) > max_data_points:
        glist.pop(0)
    
    avgg = sum(glist) / len(glist)

    dispg = '%03dg' % abs(trunc(avgg * 100))
    display.show(dispg)
#    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
#    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
#    print("Temperature: %.2f C"%mpu.temperature)
#    print('total gs: ', totalg)
#    print('display gs: ', dispg)
#    print("")
#    sleep(2)
    sleep(0.1)