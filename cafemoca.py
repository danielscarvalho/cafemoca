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
print("variance: {}".format(variance(values)))
print("average: {}".format(average(values)))
print("standard deviation: {}".format(standard_deviation(values)))


