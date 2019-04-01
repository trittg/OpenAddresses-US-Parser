import pandas as pd
import numpy as np

def format_csv(inpath, outpath, num):
    #If the csv is larger than 500 mb this program dies, very sad
    data = pd.read_csv(inpath)

    sample = data.sample(n=num, random_state=1)
    sample.to_csv(outpath, index=False)
    return