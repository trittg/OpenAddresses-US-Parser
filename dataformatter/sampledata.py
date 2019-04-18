import pandas as pd
import numpy as np

def format_csv(inpath, outpath, num):
    #If the csv is larger than 500 mb this program dies, very sad
    data = pd.read_csv(inpath, dtype=object)
    sample = data.sample(n=num, random_state=1)
    sample.reset_index(inplace=True)

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
        sample['POSTCODE'][i] = zipcode

    del sample['index']
    sample.to_csv(outpath, index=False)
    return