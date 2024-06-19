#learning about CSV files

# Importing pandas library
import pandas as pd

# Creating a dictionary
dic = {"A": [1, 2, 3, 4, 5, 6], "B": [7, 8, 9, 10, 11, 12], "C": [13, 14, 15, 16, 17, 18]}

# Creating a DataFrame from the dictionary
d = pd.DataFrame(dic)
print(d)
print("\n")

# Writing DataFrame to a CSV file
d.to_csv("dis_csv.csv")  # Saves DataFrame to a CSV file with index and header

# Writing DataFrame to a CSV file without index and with custom header
d.to_csv("dis_noindex.csv", index=False, header=[1, 2, 3])

# Reading data from a CSV file into a DataFrame
csv_1 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv")  # Use double backslashes or raw string for Windows paths
print(csv_1)
print("\n")

# Reading a row/coloum of data from a CSV file into a DataFrame
csv_2 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv", nrows=3,usecols=["A","C"])
print(csv_2)
print("\n")

# skipping a row
csv_3 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv",skiprows=[1,3])  
print(csv_3)
print("\n")

#assigning a different index , header , datatype
csv_4 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv",index_col="A")  
print(csv_4)
print("\n")

csv_5 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv",header=3)  
print(csv_5)
print("\n")

csv_6 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv",dtype={"A":"float"})  
print(csv_6)
print("\n")

# applying pandas function in CSV file

csv__1 = pd.read_csv("C:\\D\\Pandas\\example_file.csv" )  
print(csv__1)
print("\n")

#functions
print(csv__1.index)
print("\n")

print(csv__1.columns)
print("\n")

#summary of given data
print(csv__1.describe())
print("\n")

# to get upper / lower / specific rows
print(csv__1.head(2))
print("\n")

print(csv__1.tail(2))
print("\n")

print(csv__1[2:5])
print("\n")

print(csv__1.index.array)
print("\n")

print(csv__1.to_numpy())
print("\n")

#to change order of rows
print(csv__1.sort_index(axis=0,ascending=False))
print("\n")

#to change value in data
## method 1
###    print[" original value "][ index of row ]="new value"

## method 2
csv__1.loc[0,2]="new value"
print(csv__1)
print("\n")

#to access particular data
 
###  print(csv__1.loc[[2,3],[" name of partiular coloum"]])
###  print(csv__1.iloc[ index of row , index of column])

# to drop a coloum/row

print(csv__1.drop("NAME" , axis = 0))



