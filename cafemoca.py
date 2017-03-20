# App: cafemoca
# Author: @danielscarvalho
# Date: Feb/2016
# Code: main app

import cmlib

print("cafemoca app")
x1, x2 = cmlib.bhaskara(2, 6, 4)
print("x\'  = {}\nx'' = {}".format(x1, x2))

values = list(range(0,10000))

print("values: {}".format(values))
print("variance: {}".format(cmlib.variance(values)))
print("average: {}".format(cmlib.average(values)))
print("standard deviation: {}".format(cmlib.standard_deviation(values)))


