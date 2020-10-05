import time #import time for creating delay 
import Adafruit_DHT #Import DHT Library for sensor

sensor_name = Adafruit_DHT.DHT11 #we are using the DHT11 sensor
sensor_pin = 17 #The sensor is connected to GPIO17 on Pi

time.sleep(2) #wait for 2 secs

while 1: #Infinite Loop
  
    humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin) #read from sensor and save respective values in temperature and humidity varibale  
    print('temp={0:0.1f}*C humdity={1:0.1f}%'. format(temperature,humidity))
    time.sleep(2) #Wait for 2 sec then update the values
