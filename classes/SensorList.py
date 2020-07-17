import sys
sys.path.append("../")

import psycopg2
import RPi.GPIO as GPIO
from Sensor import Sensor
from config import config

class SensorList:
    
    def __init__(self):
        self.sensors = self.getSensors()
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for sensor in self.sensors:
            GPIO.setup(sensor.pin, GPIO.OUT)
            
        
    def getSensors(self):
        sensors = []
        select_query = 'select name, pin from sensor'
        connection = False
        try:
            params = config()
            connection = psycopg2.connect(**params)

            cursor = connection.cursor()
            cursor.execute(select_query)
            
            sensors_records = cursor.fetchall()
            for row in sensors_records:
                new_sensor = Sensor(row[0], row[1])
                sensors.append(new_sensor)
            
            connection.commit()
        except (Exception, psycopg2.Error) as error:
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
                msg += 'Sensor name: ' + sensor.name + '. Sensor PIN: ' + str(sensor.pin) + '\n'
        else:
            msg += 'Sensors list is empty'
        return msg

# test
sensors = SensorList()
print(sensors.message())