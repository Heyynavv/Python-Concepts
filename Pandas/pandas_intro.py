# pandas
# Whast is data manipulation ~ changing , organizing or preparing data to make it useful & easier to understand 
# to clean , transform & structure data for better usability

# what is  data analysis -- extracting patterns , trends  & insights from the data to solve problems/make decisions
#2008 

#What is pandas?
# pandas is a powerful data analysis library in Python that provides tools for data manipulation, analysis, 
# and visualization. It is built on top of NumPy and is designed to handle large, multi-dimensional data sets.
import pandas as pd
#why use pandas?
# 1. Easy to use and powerful data structures (Series, DataFrames)
# 2. Fast and efficient data manipulation and analysis

#what is series?
# A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, etc.).

#what is a dataframe?
# A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. 
# It is similar to a spreadsheet or a SQL table.

#reading data from a CSV file
df = pd.read_csv('schema.json')
# print(df)

# creating a dataframe from scratch
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)

# df.to_csv('data.csv') # to save the dataframe to a CSV file

# df.to_json('data.json') # to save the dataframe to a JSON file
