# This project uses Python's pandas, matplotlib and dash libraries 
# and showcases their use on a 50k+ record database

import pandas as pd 

# loading and cleaning data

df = pd.read_csv('data.csv', encoding="iso-8859-1")                 # read csv file using pandas

null = df.isnull().sum()                                            # get all rows with null values

zero = df.loc[(df['Longitude'] == 0) | (df['Hour'] == 0)]           # get all rows where Longitude & Hour value = 0
one = df.loc[df['Longitude'] == 1]                                  # get all rows where Longitude value = 1
zero = zero.Longitude.count()                                       # count rows from search #1
one = one.Longitude.count()                                         # count rows from search #2

zeroone = zero+one                                                  # add 2 row counts

# output a number of null or false data

print("Number of null records: \n" + str(null))
print("Number of records with false coordinates: " + str(zeroone))