"""
Cycles through each folder in the Input folder and applies city or state data
formmating toindividual files.  First filters the state files, however if no 
good data is found it will loop over all city files.

Outputs a CSV file for each state filtered address data in the output folder
"""
from dataformatter import citydata, statedata
import os

inDir = 'Input\\'
regions = os.listdir(inDir)
for r in regions:
    rpath = inDir + r + '\\us'
    states = os.listdir(rpath)
    print(rpath)
    print(states)
    for s in states:
        spath = rpath + '\\' + s
        print(spath)
        files = os.listdir(spath)
        if ('statewide.csv' in files):
            fullpath = spath + '\\statewide.csv'
            print(fullpath)
            if statedata.format_csv(fullpath) == -1:
                csvfiles = [f for f in files if f[-4:] == '.csv']
                for c in csvfiles:
                    fullpath = spath + '\\' + c
                    print(fullpath)
                    citydata.format_csv(fullpath)
        else:
            csvfiles = [f for f in files if f[-4:] == '.csv']
            for c in csvfiles:
                fullpath = spath + '\\' + c
                print(fullpath)
                citydata.format_csv(fullpath)
