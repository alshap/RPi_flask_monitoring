import sys
sys.path.append("./classes")

import timeout_decorator
import threading
import time
import psycopg2
from config import config
import datetime
from SensorList import SensorList
from DeviceList import DeviceList
from Server import MonitoringServer

postgres_query = """ INSERT INTO sensordata (sensor_id, data, time) VALUES (%s, ARRAY [%s], %s)"""

def main():
    sensorList = SensorList()
    sensorList.setup()
    deviceList = DeviceList()
    deviceList.setup()
    
    data_thread = threading.Thread(target=thread_getSendData, args=(sensorList, ))
    data_thread.start()
    web = MonitoringServer(sensorList.sensors, deviceList.devices)
    web.routes()
    web.run()
    
    
def postgre_insert(query, record):
    connection = False
    try:
        params = config()
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        cursor.execute(query, record)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print ("Connection fails", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()

def thread_getSendData(sensorList):
    print(sensorList.message())

    sensors = sensorList.sensors
    
    while True:
        for sensor in sensors:
            sensor.message()
            values = sensor.readValues()
            if str(values)[0] is not None:
                postgre_insert(postgres_query, [sensor.sensor_id, values, datetime.datetime.now()])
        time.sleep(300)
    
if __name__ == '__main__':
    main()
