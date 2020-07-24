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

## Connection schema

<details><summary>**Spoiler**</summary>

![Screenshot](https://github.com/alshap/RPi_flask_monitoring/blob/master/images/schema.png)

</details>

## Examples

Example codes for each sensor are in /examples folder.

Using example codes you can check if necessary components are working correctly.

## Implementation

### Backend

#### Data reading from sensors

### Frontend

#### Visualization and monitoring

---

## Literature

* https://pinout.xyz/
* https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
* https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
* https://www.electronicshub.org/raspberry-pi-ultrasonic-sensor-interface-tutorial/
* https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
