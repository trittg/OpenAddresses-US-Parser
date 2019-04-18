import os
from dataformatter import sampledata

testcityfile = r'Input\openaddr-collected-us_midwest\us\ia\benton.csv'
teststatefile = r'Input\openaddr-collected-us_northeast\us\ny\statewide.csv'


# citydata.format_csv(testcityfile)
# statedata.format_csv(teststatefile)

# OpenAddressRegion\us\ state or no state?


inDir = 'Output\\'
files = os.listdir(inDir)
csvfiles = [f for f in files if f[-4:] == '.csv']
for c in csvfiles:
    cpath = inDir + c
    outpath = inDir + 'Sample\\' + c
    sampledata.format_csv(cpath, outpath, 1000)
    print(cpath + '->->->' + outpath)