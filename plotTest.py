import matplotlib
import matplotlib.pyplot as plt
import csv
import numpy


x_axis_time = [5.0, 10.0, 15.0, 20.0]
y_axis_temp = [60.1, 80.2, 67.3, 50.0]

a = numpy.array([x_axis_time, y_axis_temp])
with open('myfile.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(a)
