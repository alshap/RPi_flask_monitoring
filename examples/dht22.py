import timeout_decorator
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

@timeout_decorator.timeout(5)
def main():
    try:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
    except timeout_decorator.timeout_decorator.TimeoutError:
        print("Timeout exceeded. Retrying")
            
if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)

    
    

