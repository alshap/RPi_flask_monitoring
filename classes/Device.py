import RPi.GPIO as GPIO

class Device:
    
    def __init__(self, name, pin):
        self.name = str(name)
        self.pin = int(pin)
        
    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT)
        
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        
    def getState(self):
        return GPIO.input(self.pin)
        
    def message(self):
        print('Device name: ' + self.name + '. Device PIN: ' + str(self.pin))