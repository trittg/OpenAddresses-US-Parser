"""
Takes in a CSV file with the header:
    NUMBER, STREET, CITY, STATE, POSTCODE, UNIT
Fixes zipcode entries and removes entries with invalid data for CITY and STREET
"""
import pandas as pd
import numpy as np

def format_csv(inpath, outpath, num):
    #If the csv is larger than 500 mb this program dies, very sad
    data = pd.read_csv(inpath, dtype=object)
    sample = data.sample(n=num, random_state=1)
    sample.reset_index(inplace=True)

    # format zipcode
    for i in range(len(sample['POSTCODE'])):
        zipcode = str(sample['POSTCODE'][i])
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
        # get rid of '0' value zipcodes, have not found what causes this
        if zipcode == '0':
            zipcode = np.nan
        sample['POSTCODE'][i] = zipcode


    # format Street
    for i in range(len(sample['STREET'])):
        street = str(sample['STREET'][i])
        # case street contains ',' character, then select all earlier chracters
        # sometimes the street field will contain "street, city, postcode"
        commapos = street.find(',')
        if commapos != -1:
            #print("BAD DATA:\t"+street)
            sample['STREET'][i] = np.nan
            #print(sample['STREET'][i])

    # format City
    for i in range(len(sample['CITY'])):
        city = str(sample['CITY'][i])
        # case city contains ',' character, then select all earlier chracters
        # sometimes the city field will contain "city, extra info"
        commapos = city.find(',')
        if commapos != -1:
            sample['CITY'][i] = np.nan

    sample.dropna(subset=['POSTCODE'], inplace=True)
    sample.dropna(subset=['STREET'], inplace=True)
    sample.dropna(subset=['CITY'], inplace=True)


    del sample['index']
    sample.to_csv(outpath, index=False)
    return