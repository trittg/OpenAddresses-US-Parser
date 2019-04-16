
import pandas as pd
import numpy as np
import os.path

inpath = 'dataformatter\\testcity.csv'
data = pd.read_csv(inpath, dtype=str)

print(data)

data['POSTCODE'].where(data['POSTCODE'].str.isdigit(),
                       other=(data['POSTCODE'].str.split('-')), inplace=True)



print(data)

mystr = "Hello world!"
mylist = mystr.split('-')
print(mylist)
print(mylist[0])
