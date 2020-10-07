import serial
import time
import string
import pynmea2
import os
import RPi.GPIO as GPIO
from mcp3208 import MCP3208

adc = MCP3208()

x=adc.read(0)
y=adc.read(1)
print('X:'+ str(x)+'  Y:'+str(y))
#gps = "some one is there..."
time.sleep(0.5)
x=int(x)
y=int(y)
if((x<1300) | (x> 1399)|(y<1300)|(y>1399)):
    print("stable")

else:

    print("unstablestable")