from dataformatter import citydata, statedata
import os

testcityfile = r'Input\openaddr-collected-us_midwest\us\ia\benton.csv'
teststatefile = r'Input\openaddr-collected-us_northeast\us\ny\statewide.csv'

# citydata.format_csv(testcityfile)
# statedata.format_csv(teststatefile)

inDir = 'Input\\'


regions = os.listdir(inDir)
#regions = ['openaddr-collected-us_northeast']
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
