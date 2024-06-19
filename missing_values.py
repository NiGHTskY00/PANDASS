import pandas as pd

var = pd.read_csv("C:\\D\\Pandas\\example_file.csv")
print(var)

print("\n")

# to drop missing values / functions 
print(var.dropna())

print("\n")

print(var.dropna(how="all")) #if row has all nan it will be removed
print(var.dropna(how="any")) #any row with nan will be removed
print(var.dropna(subset=["GAIN"])) # nan will be removed from givrn coloum
print(var.dropna(thresh=1)) # if row has X nan it will be removed


# to fill missing values / functions 
print(var.fillna(" filled_in"))

print(var.fillna({"GAIN":" filled_in"}))# to fill missing values of particular coloum

print(var.fillna(method="ffill")) # to fill first nan row from top 

print(var.fillna(method="bfill")) # to fill first nan row from bottom 

print(var.fillna("filled_in" , limit=1)) # to fill one nan  from a coloum

# REPLACE FUNCTION

## WAYS TO REPLACE VALUES IN DATA
print(var.replace(to_replace="nanuvut", value="passed"))

print(var.replace([1,2,3,4,5,6,7],"CH"))

print(var.replace("[A-Z]","CH",regex=True)) 

print(var.replace({"NAAVA":'[A-Z]'},"CH",regex=True)) # TO REPLACE DATA FROM A PARTICULAR COLOUM

print(var.replace(1,method="bfill"))
print(var.replace(1,method="ffill"))

print(var.replace(1,method="ffill",limit=3)) # TO replace daata within a limit

print(var.replace(1,method="ffill",limit=3,inplace=True)) # TO replace  original data 

# INTERPOLATE # IMPORTANT # works for numbers only

print(var.interpolate())

#functions
print(var.interpolate(method="linear",axis=0)) #axis 0 for coloum , axis 1 for row ## can use only when data type is same in row/coloum

print(var.interpolate(limit_direction="forward" ,limit=1)) # to interpolate some data only with limiter

var=var.infer_objects(copy=False) 
print(var.interpolate(limit_direction="forward" ,limit=1 , inplace = True))
#### IMPLACE IS USED TO CHANGE THE ORIGINAL DATA /CSV FILE
print(var)