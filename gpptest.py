import serial
import time
import string
import pynmea2
import os
import RPi.GPIO as GPIO






while True:
 port="/dev/ttyAMA0"
 ser=serial.Serial(port, baudrate=9600, timeout=0.5)

    def gps(latitude,longitude):
         dataout = pynmea2.NMEAStreamReader()
         newdata=ser.readline()

         if newdata[0:6] == b'$GPRMC':
             newmsg=pynmea2.parse(newdata.decode('ASCII'))
             lat=round(newmsg.latitude,6)
             lng=round(newmsg.longitude,6)
             gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
             print(gps)
        return gps
