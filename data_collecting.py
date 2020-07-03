import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# init dht22
DHT_SENSOR = Adafruit_DHT.DHT22

# initialize GPIO pins
DHT_PIN = 4
TRIG_PIN= 27
ECHO_PIN = 17
RESISTOR_PIN = 22

print("Initialization start")
# Setup GPIO pins
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setup(RESISTOR_PIN,GPIO.IN)
GPIO.output(TRIG_PIN, False)

print("Initialization completed")
def main():
    while True:
        humidity, temperature, light, distance = readSensorsData()
        if humidity and temperature:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
        if light:
            print("Light value: " + str(light))
        else:
            print("Failed to retrieve data from light sensor")
        if distance:
            print("Distance value: " + str(distance))
        else:
            print("Failed to retrieve data from ultrasonic sensor")
        

def readSensorsData():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    time.sleep(1)
    light = GPIO.input(RESISTOR_PIN)
    time.sleep(1)
    distance = readUltrasonicDistance()
    time.sleep(1)
    
    if humidity is None:
        humidity = False
    if temperature is None:
        temperature = False
    if light is None:
        light = False
    if distance is None:
        distance = False
    return humidity, temperature, light, distance

def readUltrasonicDistance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance+1.15, 2)
    return distance
    
if __name__ == '__main__':
    main()

