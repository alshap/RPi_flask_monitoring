import RPi.GPIO as GPIO

class Sensor:
    
    def __init__(self, name, pin, sensor_id):
        self.name = str(name)
        self.pin = int(pin)
        self.sensor_id = int(sensor_id)
        
    def setup():
        GPIO.setup(self.pin, GPIO.IN)
          
    def message(self):
        return 'Sensor name: ' + self.name + '. Sensor PIN: ' + str(self.pin)