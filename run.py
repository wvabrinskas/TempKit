#!/usr/bin/python3
import queue
import MacTmp as mt
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import threading
import sys, getopt
import numpy
import csv 

run_timer = None
end = False
export_data = False
export_filename = "data"
current_time = 0
measure_interval = 5.0
q = queue.Queue()
super_title = "Default Title"
show_graph = False

x_axis_time = []
y_axis_temp = []

def export():
  print("Exporting data to {}.csv".format(export_filename))

  a = numpy.array([x_axis_time, y_axis_temp])
  with open("{}.csv".format(export_filename), 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(a)

def plot(): 
  plt.plot(x_axis_time, y_axis_temp)

  plt.suptitle(super_title)
  title = "Total Time: {}s".format(current_time)
  plt.title(title)

  plt.xlabel('time (s)')
  plt.ylabel('temp (°F)')
  plt.show()

def measure(): 
  global current_time
  x_axis_time.append(current_time)

  temp = mt.CPU_Temp()
  split_temp = temp.split(' ') # account for some weird power string that's added

  if len(split_temp) > 0:
    y_axis_temp.append(float(split_temp[0]))
  else:
    y_axis_temp.append(float(temp))

  current_time += measure_interval  


def run(): 
  global run_timer
  measure()
  run_timer = threading.Timer(measure_interval, run)
  run_timer.start()


def done(): 
  if export_data: 
    export()

  run_timer.cancel()

  if show_graph:
    plot()
  
  print("Complete!")

def main(argv):
  global super_title
  global export_data
  global measure_interval
  global export_filename
  global show_graph

  try: 
    opts, args = getopt.getopt(argv, "hst:e:i:", ["show-graph", "title", "export", "interval"])
  except getopt.GetoptError:
    print('Error: run.py -s -t <graph_title> -e <filename> -i <measure_interval_seconds>')
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print('Help: run.py -s -t <graph_title> -e <filename> -i <measure_interval_seconds>')
      sys.exit()

    elif opt in ("-t", "--title"):
      super_title = arg
    
    elif opt in ("-e", "--export"):
      export_data = True
      export_filename = arg

    elif opt in ("-i", "--interval"):
      measure_interval = float(arg)

    elif opt in ("-s", "--show-graph"):
      show_graph = True

  print("Starting...")
  run()

  input("Press Enter to stop measurements...")
  done()

if __name__ == "__main__":
   main(sys.argv[1:])
