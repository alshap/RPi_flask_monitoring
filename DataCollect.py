import Adafruit_DHT
import RPi.GPIO as GPIO
import time

class DataCollect:
    
    DHT_SENSOR = Adafruit_DHT.DHT22
    
    def __init__(self, DHT_PIN = 0, ECHO_PIN = 0, TRIG_PIN = 0, RESISTOR_PIN = 0):
        self.DHT_PIN = DHT_PIN
        self.ECHO_PIN = ECHO_PIN
        self.TRIG_PIN = TRIG_PIN
        self.RESISTOR_PIN = RESISTOR_PIN
        
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.TRIG_PIN,GPIO.OUT)
        GPIO.setup(self.ECHO_PIN,GPIO.IN)
        GPIO.setup(self.RESISTOR_PIN,GPIO.IN)
        GPIO.output(self.TRIG_PIN, False)
    
    def readUltrasonicDistance(self):
        GPIO.output(self.TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG_PIN, False)

        while GPIO.input(self.ECHO_PIN)==0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO_PIN)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance+1.15, 2)
        return distance
    
    def readTemperatureHumidity(self):
        humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
        if humidity is not None and temperature is not None:
            return temperature, humidity
        else:
            return None
        
    def readPhotoresistorValue(self):
        light_value = GPIO.input(self.RESISTOR_PIN)
        if light_value is not None:
            return light_value
        else:
            return None
        


  
