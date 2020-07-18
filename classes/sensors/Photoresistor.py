import sys
sys.path.append("../")
import RPi.GPIO as GPIO
from Sensor import Sensor

from Sensor import Sensor

class Photoresistor(Sensor):
    
    def readValues(self):
        light = GPIO.input(self.pin)
        if light is not None:
            return light
        else:
            return None
        