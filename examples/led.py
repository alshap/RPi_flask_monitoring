import RPi.GPIO as GPIO
import time

LED_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED_PIN,GPIO.OUT)

def main():
    try:
        GPIO.output(LED_PIN,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN,GPIO.LOW)
    except KeyboardInterrupt:
     GPIO.cleanup() 

if __name__ == '__main__':
    main()