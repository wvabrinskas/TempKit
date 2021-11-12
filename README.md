# TempKit 
This is a simple CLI tool that can be used to measure and plot system temperatures over time on macOS. 

[![Python 3.9.7](https://img.shields.io/badge/python-3.9.7-blue.svg)](https://www.python.org/downloads/release/python-397/)

# Installation 
## Requirements
These can be installed using `pip3` 
- matplotlib
- MacTmp

# Usage 
run `python3 run.py -s -t "Cool Graph Title" -e "output" -i 5`

## Parameters
All parameters are optional
- `-h`
  - Shows the help information 
- `-i` or `--interval` 
  - Sets the polling interval in seconds for temperature readings `(default: 5.0)`
- `-s` or `--show-graph`
  - Will bring up a interactive graph of the collected data points
- `-t` or `--title`
  - Sets the title of the graph 
- `-e` or `--e` 
  - Name of the file to export the data to. Do not include the extension. Outputs as `csv`
  - Not setting this will result in the program not exporting your data to a CSV. 