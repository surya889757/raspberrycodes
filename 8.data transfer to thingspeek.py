
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
    return (str(RH), str(T))
while True:
	    baseURL = 'https://api.thingspeak.com/update?api_key=APAQPR0VA8KDWWSA'
            RH, T = getSensorData()
            payload = '{"temperature": ' + (T) + ',"humidity": '+ (RH) + ' }'
            print payload 
            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s" % (T, RH))
            print f.read()
            f.close()
            sleep(15)
	


