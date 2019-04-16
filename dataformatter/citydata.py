"""
Takes in a single csv file of a city with the header of
'1    2    3       4       5     6     7         8       9         10  11'
'LON, LAT, NUMBER, STREET, UNIT, CITY, DISTRICT, REGION, POSTCODE, ID, HASH'

OUTPUT
Outputs a csv file with the hardcoded specific header
OLD POS: 3       4         6           NONE,  9       , 7
         NUMBER, STREET,   CITY,       STATE, POSTCODE, UNIT
EXAMPLE  5516,   Co Rd 27, Fort Payne, AL,    35968,    6134
"""

import pandas as pd
import numpy as np
import os.path


def format_csv(inpath, outpath='Output\\'):
    """
    Given the filepath to a csv file for a cities addresses will output a new
    csv file with the relevant information formatted

    Inpath: file path to a csv file
    Outpath: file path to the output dir
    """
    state = parsestate(inpath)
    cityname = parsecity(inpath)
    goodcols = ['NUMBER', 'STREET', 'CITY', 'POSTCODE', 'UNIT']
    data = pd.read_csv(inpath, dtype=str, usecols=goodcols)

    print("Reading file: ", inpath)
    # reorder dataframe
    newdata = data[goodcols]
    # remove rows that are missing non-optional data
    newdata = newdata.dropna(subset=['STREET', 'POSTCODE'])
    # insert new STATE column
    newdata.insert(3, 'STATE', state)
    # fill empty CITY column values
    newdata = newdata.fillna({'CITY': cityname})
    # check if dataframe is empty - can't clean empty data
    if newdata.empty:
        print(cityname + " is empty...")
    else:
        # clean data in NUMBER and UNIT column
        newdata['UNIT'] = newdata['UNIT'].where(newdata['UNIT'].str.isdigit())
        newdata['NUMBER'] = newdata['NUMBER'].where(
            newdata['NUMBER'].str.isdigit())
    filename = outpath + state + '.csv'
    if os.path.isfile(filename):
        newdata.to_csv(filename, index=False, mode='a', header=False)
        print("File appended to: " + filename)
    else:
        newdata.to_csv(filename, index=False)
        print("File printed to: " + filename)
    return


def parsestate(path):
    """
    returns the state from the given file path
    """
    return path.split('\\')[3].upper()


def parsecity(path):
    """
    returns the city name from the given file path
    """
    city = path.split('\\')[4]
    # remove file type
    city = city[:-4]
    # remove possible prefix
    cityprefix = 'city_of_'
    if (city.startswith(cityprefix)):
        city = city[len(cityprefix):]
    # remove underscores and capitalize city name
    city = city.replace('_', ' ').title()
    return city
