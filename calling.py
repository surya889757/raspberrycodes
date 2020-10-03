import serial
import os, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)




port.write(b'AT\r')
rcv = port.read(10)
print(rcv)
            
time.sleep(1)

port.write(b'ATD8328034196;\r')
print("Calling…")
time.sleep(30)
port.write(b'ATH\r')
print("Hang Call…")


