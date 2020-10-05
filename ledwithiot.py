# Import standard python modules
import time
import RPi.GPIO as GPIO
import time
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

P_LED = 21    # adapt to your wiring
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(P_LED,GPIO.OUT)
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '065ee7ff3ccd414eabae15673c4ae70d'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'takeoff'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('l1')
except RequestError: # create a digital feed
    feed = Feed(name="l1")
    digital = aio.create_feed(feed)

while True:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
        GPIO.output(P_LED,GPIO.HIGH)
    elif int(data.value) == 0:
        print('received <- OFF\n')
        GPIO.output(P_LED,GPIO.LOW)

   
    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)
