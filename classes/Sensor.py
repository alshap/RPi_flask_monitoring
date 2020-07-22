import sys
sys.path.append("../")

import RPi.GPIO as GPIO
import psycopg2
import datetime
from config import config
from dateutil import parser

class Sensor:
    
    def __init__(self, name, pin, sensor_id):
        self.name = str(name)
        self.pin = int(pin)
        self.sensor_id = int(sensor_id)
        
    def setup():
        GPIO.setup(self.pin, GPIO.IN)
          
    def message(self):
        return 'Sensor name: ' + self.name + '. Sensor PIN: ' + str(self.pin)
    
    def getDataOnPeriod(self, datefrom, dateto):
        datefrom = parser.parse(datefrom)
        dateto = parser.parse(dateto)
        data = []
        select_query = 'select name, data, time from sensordata inner join sensor on sensordata.sensor_id = ' + str(self.pin)
        print(select_query)
        connection = False
        try:
            params = config()
            connection = psycopg2.connect(**params)

            cursor = connection.cursor()
            cursor.execute(select_query)
            
            data_records = cursor.fetchall()
            for row in data_records:
                data.append({"sensor": row[0], "data": row[1], "time": row[2]})
            
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print('Error in db')
            return []
        finally:
            if(connection):
                cursor.close()
                connection.close()
            return data
       
    
    def readValues(self):
        pass
# test 
# sensor = Sensor('DHT22', 4, 4)
# print(sensor.getDataOnPeriod('18-07-2020', '24-09-2020'))