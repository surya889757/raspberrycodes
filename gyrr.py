import serial
import time
import string
import pynmea2
import os
import RPi.GPIO as GPIO





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
     ser.write(b'AT+CMGS="8328034196"\r')

     print("sending sms…")
     time.sleep(3)
     ser.reset_output_buffer()
     time.sleep(1)
     
     ser.write(str.encode(gps+chr(26)))
     time.sleep(1)

     print (gps)
     print("msg sent...")

