# App: cafemoca
# Author: @danielscarvalho
# Date: Feb/2016
# Code: cf lib

import math

# bhaskara calculation: http://mathworld.wolfram.com/QuadraticEquation.html 
def bhaskara(a, b, c):
    x=math.sqrt((b**2)-(4*a*c))
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
    return x1, x2

# Statistics: Average: http://mathworld.wolfram.com/Mean.html 
def average(values):
    vsum = sum(values)
    itens = len(values)
    return vsum / float(itens)

# Statistics: Variance: http://mathworld.wolfram.com/Variance.html
def variance(values):
    vaverage = average(values)
    vsum = 0
    vvariance = 0

    for value in values:
        vsum += math.pow( (value - vaverage), 2)
    
    vvariance = vsum / float( len(values) )
    
    return vvariance

# Statistics: Standard Deviation: http://mathworld.wolfram.com/StandardDeviation.html:
def standard_deviation(values):
    return math.sqrt(variance(values))


