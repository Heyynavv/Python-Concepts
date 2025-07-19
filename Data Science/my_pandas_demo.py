#Pandas

# pandas is how we read & process data in python 


#DataFrame & Series
# Pandas tables are called dataframes & each column from which the
# DF is made up of is a series

import pandas as pd

import numpy as np

a = [[1,2] , [ 3,4]]
np.array(a)
print(a)

b  = pd.DataFrame(a)
print(b)
#creating a dataframe
c = pd.DataFrame([{"maths" : 60 , "science": 80 } , {"maths" : 100 , "science": 95 }])
print(c)
print(c["maths"])

# head & tail 
print(c.head(1))

#Data formats
# Pandas can read data from SQL , CSV , EXCEL , JSON etch 
# .csv --- a plain text tabular only format
# .json --- dictionary based plain text data format 
# .xlsx & .pkl

# reading a data

# countries_covid_data = pd.read_csv("C:\Users\hp\Desktop\Python2.0\Data Science\Random Covid - 19 data\countries-aggregated.csv")

# Use Raw String Literal (Recommended) 



countries_covid_data = pd.read_csv(r"C:\Users\hp\Desktop\Python2.0\Data Science\Random data\countries-aggregated.csv")


# pd.set_option('display.max_rows', None)       # Show all rows
# pd.set_option('display.max_columns', None)    # Show all columns
# pd.set_option('display.width', None)          # Don't cut off wide tables
# pd.set_option('display.max_colwidth', None)   # Show full content of each column

print(countries_covid_data)

print(countries_covid_data.info())

#pandas indices 

print(countries_covid_data.loc[161565])

print(countries_covid_data.set_index("Country").loc["India"])


