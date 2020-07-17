import RPi.GPIO as GPIO

class Device:
    
    def __init__(self, name, pin):
        self.name = str(name)
        self.pin = int(pin)
        
    def setup():
        GPIO.setup(self.pin, GPIO.OUT)
        
    def on():
        GPIO.output(self.pin, GPIO.HIGH)
    
    def off():
        GPIO.output(self.pin, GPIO.LOW)
        
    def message(self):
        print('Device name: ' + self.name + '. Device PIN: ' + str(self.pin))