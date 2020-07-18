import sys
sys.path.append("../")
import Adafruit_DHT

from Sensor import Sensor

class DHT22(Sensor):
    
    DHT_SENSOR = Adafruit_DHT.DHT22
    
    def readValues(self):
        humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.pin)
        if humidity is not None and temperature is not None:
            humidity = round(humidity, 2)
            temperature = round(temperature, 2)
            return temperature, humidity
        else:
            return None, None
        
        
        