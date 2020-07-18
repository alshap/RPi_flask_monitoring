import sys
sys.path.append("../")
sys.path.append("/home/pi/Desktop/flask_server/classes/sensors")

import psycopg2
import RPi.GPIO as GPIO
from Sensor import Sensor
from config import config
import time

class SensorList():
    
    def __init__(self):
        self.sensors = self.getSensors()
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for sensor in self.sensors:
            GPIO.setup(sensor.pin, GPIO.OUT)
            
        
    def getSensors(self):
        sensors = []
        select_query = 'select name, pin, sensor_id from sensor'
        connection = False
        try:
            params = config()
            connection = psycopg2.connect(**params)

            cursor = connection.cursor()
            cursor.execute(select_query)
            
            sensors_records = cursor.fetchall()
            for row in sensors_records:
                try:
                    exec('from ' + row[0] + ' import ' + row[0])
                    new_sensor = eval(row[0])(row[0], row[1], row[2])
                    if new_sensor:
                        sensors.append(new_sensor)
                except Exception:
                    pass
            
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            print('Error in db')
            return []
        finally:
            if(connection):
                cursor.close()
                connection.close()
            return sensors
           
    
    def message(self):
        msg = ''
        if self.sensors:
            for sensor in self.sensors:
                msg += 'ID: ' + str(sensor.sensor_id) + '. Sensor name: ' + sensor.name + '. Sensor PIN: ' + str(sensor.pin) + '\n'
        else:
            msg += 'Sensors list is empty'
        return msg

# test
#sensors = SensorList()
#print(sensors.message())
#sensors.setup()
#for sensor in sensors.sensors:
#    while True:
#        time.sleep(1)
#        print(sensor.readValues())