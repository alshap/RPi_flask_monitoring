import RPi.GPIO as GPIO
import time
import timeout_decorator


GPIO.setmode(GPIO.BCM)

TRIG_PIN = 27
ECHO_PIN = 17

GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)

GPIO.output(TRIG_PIN, False)
time.sleep(2)

@timeout_decorator.timeout(5)
def main():
    try:
        while True:
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
           print(distance)
    except KeyboardInterrupt:
         GPIO.cleanup()

if __name__ == '__main__':
    main()
    time.sleep(1)
