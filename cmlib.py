# App: cafemoca
# Author: @danielscarvalho
# Date: Feb/2016
# Code: cf lib
import math
 
def bhaskara(a, b, c):
    x=math.sqrt((b**2)-(4*a*c))
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
    return x1, x2

def standard_deviation(values):
    return math.sqrt(variance(values))
