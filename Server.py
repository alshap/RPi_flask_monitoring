import sys
sys.path.append("./classes")
from SensorList import SensorList
import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template, request, url_for, redirect


class MonitoringServer():

    def __init__(self, sensors = [], devices = []):
        self.application = Flask(__name__)
        self.sensors = sensors
        self.devices = devices
        
    def routes(self):
        
        @self.application.route('/sorted_data/<datefrom>-<dateto>')
        def sorted_data(datefrom, dateto):
            return 'Date from: %s Date to: %s' % (datefrom, dateto)
        
        @self.application.route('/',methods = ['POST', 'GET'])
        def index():
            try:
                if request.method == 'POST':
                    if request.form['red_led']:
                        for x in self.devices:
                            if x.name == 'red_led':
                                if x.getState(): self.devices[0].off()
                                else: x.on()
                elif request.method == 'GET':
                    if request.args['DateFrom']:
                        datefrom = request.args['DateFrom']
                    else:
                        datefrom = 0
                    if request.args['DateTo']:
                    dateto = request.args['DateTo']
                    else:
                        dateto = datetime.now()
                    return redirect(url_for('sorted_data',datefrom = datefrom, dateto = dateto))
                    
                return render_template('template.html')
            except Exception as e:
                return render_template('template.html')
                
        
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
        self.application.run(debug=True, threaded=True)
        
