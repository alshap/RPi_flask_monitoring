import timeout_decorator
from DataCollect import DataCollect
import time
import psycopg2
from config import config
import datetime

postgres_query = """ INSERT INTO sensordata (sensor_id, data, time, value_type) VALUES (%s, %s, %s, %s)"""


data_collection = DataCollect(DHT_PIN = 4, ECHO_PIN = 17, TRIG_PIN = 27, RESISTOR_PIN = 22)
data_collection.setup()

def main():
    distance = ultrasonic_value()
    temperature, humidity = temperature_humidity_value()
    light = photoresistor_value()
    if temperature is not None and humidity is not None:
        postgre_insert(postgres_query, [1, temperature, datetime.datetime.now(), 'celsius'])
        postgre_insert(postgres_query, [1, humidity, datetime.datetime.now(), 'percent'])
    if distance is not None:
        postgre_insert(postgres_query, [2, distance, datetime.datetime.now(), 'cm'])
    if light is not None:
        postgre_insert(postgres_query, [3, light, datetime.datetime.now(), 'bool'])

@timeout_decorator.timeout(5)
def ultrasonic_value():
    try:
        distance = data_collection.readUltrasonicDistance()
        return distance
    except timeout_decorator.timeout_decorator.TimeoutError:
        print("Timeout exceeded. Retrying")

@timeout_decorator.timeout(5)
def temperature_humidity_value():
    try:
        temperature, humidity = data_collection.readTemperatureHumidity()
        return temperature, humidity
    except timeout_decorator.timeout_decorator.TimeoutError:
        print("Timeout exceeded. Retrying")

@timeout_decorator.timeout(5)
def photoresistor_value():
    try:
        light = data_collection.readPhotoresistorValue()
        return light
    except timeout_decorator.timeout_decorator.TimeoutError:
        print("Timeout exceeded. Retrying")
        
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
            
if __name__ == '__main__':
    while True:
        main()
