import sys
sys.path.append("./classes")
from SensorList import SensorList
import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template, request


class MonitoringServer():

    def __init__(self, sensors = [], devices = []):
        self.application = Flask(__name__)
        self.sensors = sensors
        self.devices = devices
        
    def routes(self):
        
        @self.application.route('/',methods = ['POST', 'GET'])
        def index():
            if request.method == 'POST':
                if request.args.get('red_led'):
                    if self.devices[0].getState(): self.devices[0].on()
                    else: self.devices[0].off()
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
        
