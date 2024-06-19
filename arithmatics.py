#learning about aritmatic operations in pandas

import pandas as pd
var = pd.DataFrame({"A": [1,2,3,4],"B":[11,12,13,14]})
print(var)
print("\n"*2)

#addition
var["C"] = var["A"] + var["B"]
print(var)
print("\n"*2)

#multiplication
var["C"] = var["A"] * var["B"]
print(var)
print("\n"*2)

#division
var["C"] = var["A"] / var["B"]
print(var)
print("\n"*2)

#using operators <,> 
var1 = pd.DataFrame({"A": [10,20,30,40],"B":[15,16,17,18]})
print(var1)
print("\n"*2)

var1["A<=20"] = var1["A"] <= 20
var1["B>=16"] = var1["B"] >= 16
print(var1)

# Reading data from a CSV file into a DataFrame
csv_1 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv")  # Use double backslashes or raw string for Windows paths
print(csv_1)
print("\n")

# Reading only the first row of data from a CSV file into a DataFrame
csv_2 = pd.read_csv("C:\\D\\Pandas\\dis_csv.csv", nrows=1)
print(csv_2)
print("\n")

## 