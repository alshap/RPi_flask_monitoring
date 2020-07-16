import RPi.GPIO as GPIO
import time
import timeout_decorator

RESISTOR_PIN = 22

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RESISTOR_PIN,GPIO.IN)

@timeout_decorator.timeout(5)
def main():
    try:
        light_value = GPIO.input(RESISTOR_PIN)
        print (" Light value: " + str(light_value))
    except timeout_decorator.timeout_decorator.TimeoutError:
        print("Timeout exceeded. Retrying")
         
if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
