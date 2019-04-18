
import pandas as pd
import numpy as np
import os.path

inpath = 'dataformatter\\testcity.csv'
newdata = pd.read_csv(inpath, dtype=str)

print(newdata)

print(len(newdata['POSTCODE']))
for i in range(len(newdata['POSTCODE'])):
    zipcode = str(newdata['POSTCODE'][i])
    # case zipcode contains - character, then select all earlier chracters
    hypenpos = zipcode.find('-')
    if hypenpos != -1:
        zipcode = zipcode[:hypenpos]
    # case zipcode contains illegal chracter, then drop the value
    if not zipcode.isdigit():
        zipcode = np.nan
    # case zipcode is larger than 5 digits (assume it has the 4 digit routing code)
    # only take the characters before the 4 digit routing number
    elif len(zipcode) > 5:
        zipcode = zipcode[:-4]
    newdata['POSTCODE'][i] = zipcode
print(newdata)