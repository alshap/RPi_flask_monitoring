import random

import sys
sys.path.append("../")

from Sensor import Sensor

class ValuesTest2(Sensor):
    
    def readValues(self):
        return [random.randint(41, 67), random.randint(5, 41)]
        
        
        