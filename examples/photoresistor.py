import RPi.GPIO as GPIO
import time

RESISTOR_PIN = 22

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RESISTOR_PIN,GPIO.IN)

def main():
    while True:
        try:
            light_value = GPIO.input(RESISTOR_PIN)
            print (" Light value: " + str(light_value))
            time.sleep(1)
        except KeyboardInterrupt:
         GPIO.cleanup()
         
if __name__ == '__main__':
    main()
