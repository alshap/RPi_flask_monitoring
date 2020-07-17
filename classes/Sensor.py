import RPi.GPIO as GPIO

class Sensor:
    
    def __init__(self, name, pin):
        self.name = str(name)
        self.pin = int(pin)
        
    def setup():
        GPIO.setup(self.pin, GPIO.IN)
          
    def message(self):
        print('Sensor name: ' + self.name + '. Sensor PIN: ' + str(self.pin))