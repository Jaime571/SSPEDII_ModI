import math
from decimal import Decimal

class polarData:
    def __init__(self, magnitude = 0, direction = 0):
        self.magnitude = magnitude
        self.direction = direction

    def getMagnitude(self):
            return self.magnitude
    
    def setMagnitude(self, magnitude):
            self.magnitude = magnitude
        
    def getDirection(self): 
        return self.direction
    
    def setDirection(self, direction): 
        self.direction = direction
    
    def toRadian(self):
        return self.direction * (3.1415 / 180)
    
    def toRectangularData(self):
        x = self.magnitude * math.cos(self.toRadian())
        y = self.magnitude * math.sin(self.toRadian())
        return (x, y)
    
def toPolarData(result):
     magnitude = math.sqrt(math.pow(result.get('x'), 2) + math.pow(result.get('y'), 2))
     direction = math.degrees(math.atan(result.get('y') / result.get('x')))
     return (magnitude, direction)
    
    

    
