"""
Takes a sample of n addresses from any csv files in the output folder (created 
by main.py) Applies a final filter and removal of invalid data and outputs the 
sample data into the sample folder.
"""

import os
from dataformatter import sampledata

samples = 1000
inDir = 'Output\\'
files = os.listdir(inDir)
csvfiles = [f for f in files if f[-4:] == '.csv']
for c in csvfiles:
    cpath = inDir + c
    outpath = inDir + 'Sample\\' + c
    sampledata.format_csv(cpath, outpath, samples)
    print(cpath + '->->->' + outpath)
