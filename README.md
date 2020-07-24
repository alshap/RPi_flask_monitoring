# Raspberry Pi data web monitoring using Flask

## Introduction

This project is a Flask web server implementation on Raspberry Pi to monitor data collected from sensors. 

Raspberry Pi collects data from sensors then saves it in Postgree database and also sends data to web server to monitor data in real time. Using saved data in Postgree happens data monitoring on certain period. Also using web interface can be controlled devices connected to Raspberry Pi and they can be turned on/off.

All necessary code to project implementation can be found here:
1. Postgree db dump in folder /db
2. Example codes in folder /examples
3. implemented classes for devices and sensors in /classes
4. Frontend .html templates in folder /templates
5. Web server code in file Server.py
6. Executive file is main.py

**Project is on Python 3.x version**

## Connection schema

<details><summary>**Spoiler**</summary>

![Screenshot](https://github.com/alshap/RPi_flask_monitoring/blob/master/images/schema.png)

</details>

## Examples

Example codes for each sensor are in /examples folder.

Using example codes you can check if necessary components are working correctly.

## Implementation

### Environment preparation

Firstly install all necessary packages

DHT22 library for reading values from this sensor
```
sudo pip3 install Adafruit_DHT
```

Flask web server library
```
sudo pip3 install Flask
```

Raspberry Pi GPIO control library
```
sudo pip3 install gpiozero
```

Postgree database client for local database control using command prompt
```
sudo apt install postgresql libpq-dev postgresql-client
```

Decorator to create timeout for function execution
```
sudo pip3 install timeout_decorator
```

Library to work with Date and Time data types
```
sudo pip3 install python-dateutil
```

### Backend

#### Data reading from sensors

To work with sensors were created Sensor and SensorList classes. 

Sensor has got subclasses for each sensor we are using.

By using classes were implemented necessary functions to work with each sensor. Each Sensor has got folloing functions:

* message() to display information about sensor
* getDataOnPeriod(datefrom, dateto) to get from database data about sensor records on certain period
* readValues() to read data from sensor

SensorList class implements function to work with List of Sensors:

* getSensors() - to read all connected Sensors from database
* message() - to display all sensors information
* setup() - to setup all sensors

#### Devices control

To work with devices were created Device and DeviceList classes.

Device class allows to control all devices using same functions
This class have following opportunities:

* on() to turn device on
* off() to turn device off
* getState() to check if device turned on/off
* message() to get information about device

DeviceList class were created to get Devices from database and have following functions:

* setup() to setup all devices pins
* getDevices() to get devices list from database
* message() to display information about all connected devices

### Frontend

#### Visualization and monitoring

---

## Literature

* https://pinout.xyz/
* https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
* https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
* https://www.electronicshub.org/raspberry-pi-ultrasonic-sensor-interface-tutorial/
* https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
* https://www.postgresqltutorial.com/postgresql-python/connect/
* https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi



