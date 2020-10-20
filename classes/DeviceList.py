import sys
sys.path.append("../")

import psycopg2
import RPi.GPIO as GPIO
from Device import Device
from config import config
from time import sleep

class DeviceList():
    
    def __init__(self):
        self.devices = self.getDevices()
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for device in self.devices:
            GPIO.setup(device.pin, GPIO.OUT)
            
        
    def getDevices(self):
        devices = []
        select_query = 'select name, pin from device'
        connection = False
        try:
            params = config()
            connection = psycopg2.connect(**params)

            cursor = connection.cursor()
            cursor.execute(select_query)
            
            devices_records = cursor.fetchall()
            for row in devices_records:
                new_device = Device(row[0], row[1])
                devices.append(new_device)
            
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print('Error in db')
            return []
        finally:
            if(connection):
                cursor.close()
                connection.close()
            return devices
           
    
    def message(self):
        msg = ''
        if self.devices:
            for device in self.devices:
                msg += 'Device name: ' + device.name + '. Device PIN: ' + str(device.pin) + '\n'
        else:
            msg += 'Devices list is empty'
        return msg

# test
devices = DeviceList()
print(devices.message())
#devices.setup()
#for device in devices.devices:
#    while True:
#        device.on()
#        sleep(1)
#        device.off()
#        sleep(1)
