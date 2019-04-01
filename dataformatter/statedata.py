"""
Takes in a single csv file of a state with the header of
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


def format_csv(inpath, outpath='Output\\'):
    """
    Given the filepath to a csv file for statewide addresses will output a new
    csv file with the relevant information formatted

    Inpath: file path to a csv file
    Outpath: file path to the output dir

    return 0: everything good
           1: Empty dataframe, reccomend calling file search individual cities
              files
    """
    state = parsestate(inpath)
    searchcities = 0
    goodcols = ['NUMBER', 'STREET', 'CITY', 'POSTCODE', 'UNIT']
    data = pd.read_csv(inpath, dtype=str, usecols=goodcols)

    print("Reading file: ", inpath)
    # reorder dataframe
    newdata = data[goodcols]
    # remove rows that are missing non-optional data
    newdata = newdata.dropna(subset=['STREET', 'CITY', 'POSTCODE'])
    # insert new STATE column
    newdata.insert(3, 'STATE', state)
    # check if dataframe is empty - no good data in state file
    if newdata.empty:
        print(state + " is empty, consider searching cities")
        searchcities = -1
    else:
        # clean data in NUMBER and UNIT column
        newdata['UNIT'] = newdata['UNIT'].where(newdata['UNIT'].str.isdigit())
        newdata['NUMBER'] = newdata['NUMBER'].where(
            newdata['NUMBER'].str.isdigit())

    filename = outpath + state + '.csv'
    print("File printed to: " + filename)
    newdata.to_csv(filename, index=False)
    return searchcities


def parsestate(path):
    """
    returns the state from the given file path
    """
    return path.split('\\')[3].upper()
