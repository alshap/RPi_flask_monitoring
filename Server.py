import sys
sys.path.append("./classes")
from SensorList import SensorList
import json
import random
import time
from datetime import datetime
from dateutil import parser

from flask import Flask, Response, render_template, request, url_for, redirect


class MonitoringServer():

    def __init__(self, sensors = [], devices = []):
        self.application = Flask(__name__)
        self.sensors = sensors
        self.devices = devices
        
    def routes(self):
        @self.application.route('/sorted_data/<selected_sensor>&<datefrom>&<dateto>')
        def sorted_data(datefrom, dateto, selected_sensor):
            records = []
            for sensor in self.sensors:
                if sensor.name == selected_sensor:
                    records.append(sensor.getDataOnPeriod(datefrom, dateto))
            times = []
            values = []
            for device_records in records:
                for record in device_records:
                    if type(record['data'][0]) == type([]):
                        for i in range(0, len(record['data'][0])):
                            values.append(record['data'][0][i])
                            times.append(record['time'])
                    elif type(record['data'][0]) == type(1.5):
                        values.append(record['data'][0])
                        times.append(record['time'])
            title = 'Sensor: ' + selected_sensor + '\n From ' + datefrom + ' To ' + dateto
            return render_template('sorted_data.html',title=title, values=values, labels=times, max=20)
            
        
        @self.application.route('/',methods = ['POST', 'GET'])
        def index():
#             sensors template = [{name: name, title: title}]
            sensors_template = {}
            idx = 0
            for sensor in self.sensors:
                sensors_template[idx] = {'name': sensor.name,'labels': sensor.labels}
                idx += 1
                
            devices_template = {}
            idx = 0
            for device in self.devices:
                devices_template[idx] = {'name': device.name, 'status': device.getState()}
                idx += 1
                
            try:
                if request.method == 'POST':
                    for device in self.devices:
                        try:
                            if request.form[device.name]:
                                if device.getState(): device.off()
                                else: device.on()
#                               ---
                                devices_template = {}
                                idx = 0
                                for device in self.devices:
                                    devices_template[idx] = {'name': device.name, 'status': device.getState()}
                                    idx += 1
#                               ---
                                break
                        except Exception as ex:
                            pass
                            
                            
#                     if request.form['red_led']:
#                         for x in self.devices:
#                             if x.name == 'red_led':
#                                 if x.getState(): self.devices[0].off()
#                                 else: x.on()
                elif request.method == 'GET':
                    if request.args['SelectedSensor']:
                        selected_sensor = request.args['SelectedSensor']
                    else:
                        return render_template('template.html', sensors = sensors_template, devices = devices_template)
                    if request.args['DateFrom']:
                        datefrom = request.args['DateFrom']
                    else:
                        datefrom = 0
                    if request.args['DateTo']:
                        dateto = request.args['DateTo']
                    else:
                        dateto = datetime.now()
                    return redirect(url_for('sorted_data',datefrom = datefrom, dateto = dateto, selected_sensor = selected_sensor))
                
                return render_template('template.html', sensors = sensors_template, devices = devices_template)
                    
            except Exception as e:
                return render_template('template.html', sensors = sensors_template, devices = devices_template)
                
        
        @self.application.route('/chart-data')
        def chart_data():
            def generate_data():
                while True:
                    for sensor in self.sensors:
                        value = sensor.readValues()
                        if str(value)[0] is not None:
                            json_data = json.dumps(
                                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': value, 'sensor': sensor.name})
                            yield f"data:{json_data}\n\n"
                            time.sleep(2)
                        else:
                            pass

            return Response(generate_data(), mimetype='text/event-stream')
        
    def run(self):
        self.application.run(debug=True, threaded=True, host='0.0.0.0')
        
#sensors = SensorList()
#for sensor in sensors.sensors:
#    if (sensor.name == 'DHT22'):
#        dht22 = sensor
#    elif (sensor.name == 'Photoresistor'):
#        photoresistor = sensor

#datad = dht22.getDataOnPeriod('22-07-2020', '24-07-2020')
#datap = photoresistor.getDataOnPeriod('20-07-2020', '24-07-2020')
#print(type(datad[0]['data'][0]))
#print(type(datap[0]['data'][0]))
#print(datad[0])
#print(datap[0])
#if type(datad[0] == type([])):
#    print('list')