import random

import sys
sys.path.append("../")

from Sensor import Sensor

class ValuesTest(Sensor):
    
    def readValues(self):
        return [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
        
        
        