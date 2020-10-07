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
     while True:
         port="/dev/ttyAMA0"
         ser=serial.Serial(port, baudrate=9600, timeout=0.5)
         dataout = pynmea2.NMEAStreamReader()
         newdata=ser.readline()
         
         if newdata[0:6] == b'$GPRMC':
             newmsg=pynmea2.parse(newdata.decode('ASCII'))
             lat=round(newmsg.latitude,6)
             lng=round(newmsg.longitude,6)
             gps = "some one is there...Latitude=" + str(lat) + "and Longitude=" + str(lng)
             
             
             ser.write(b'AT\r')
             rcv=ser.read(10)
             print(rcv)
             time.sleep(1)
             
             ser.write(b"AT+CMGF=1\r")
             print("Text Mode Enabled…")
             time.sleep(3)
             ser.write(b'AT+CMGS="9494866093"\r')
             print("sending sms…")
             time.sleep(3)
             
             ser.reset_output_buffer()
             time.sleep(1)
             ser.write(str.encode(gps+chr(26)))
             time.sleep(1)
             print(gps)
             print("msg sent...")
