# OpenAddresses-US-Parser
Python program to format USA state addresses from USA region datasets taken from openaddress.io. Where the dataset from openaddress.io is split up between either state or city files this program combs through the statewide files (if present).  If no usuable data is found in the stae file then it will then search through each city file.  The end result is a csv file for each of the 50 states with the following header. 
```
    'NUMBER', 'STREET', 'CITY', 'POSTCODE', 'UNIT'
```

## Prerequisites

### Dependencies
Python 3 and pandas are required to run this project

Command to install pandas
```
pip install pandas
```
### Input
Download US region data from openaddress.io and unzip the contents in the Input folder, be sure to give each region its own folder.

ex.) .\\Input\\openaddr-collected-us_midwest\\...

### Input File Structure
    .
    ├── dataformatter           # Modules for formatting data
    ├── Input                   # US region data from open address.io
    |       └── Regiondata 1
    |       └── Regiondata ...
    |       └── Regiondata n
    ├── Output                  # CSV file per state
    |       └── Sample          # Sample selection and final filtered CSV files per state
    ├── main.py
    ├── sample.py
    └── README.md


## Running the Program

To use this tool make sure you have downloaded the region data and placed it in the Input folder.  Run the main.py file to compile all state address data in the Output folder.  Run the sample.py file to select x sample addresses from each state, apply the final filter and out put the remaining valid data entries in the sample folder.  By default the sample.py takes a sample of 1000 addresses from each state csv file.

