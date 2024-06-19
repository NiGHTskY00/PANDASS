###nPandas is most commonly used for data wrangling and data manipulation purposes, and NumPy objects are primarily used to create arrays or matrices that can be applied to DL or ML models.

#learning about data structures in pandas 
#1 series(1-D data)

#basic examples


import pandas as pd

x = [3,4,5,6,7,8]
var = pd.Series(x,index=["a","b","c","d","e","f"], dtype="float",name="series-one")
print("example 1")
print(var)
print(type(var))
print('\n' * 5)

#dictonary to series example

dic = {"name": ['python','c++','java'],"pop":[12,16,15],"rank":[1,4,3]}
var1 = pd.Series(dic)
print("example 2")
print(var1)
print('\n' * 5)

#multiple blocks of single variable

s=pd.Series(12,index=["a","b","c","d","e","f"],)
print("example 3")
print(s)
print(type(s))
print('\n' * 5)

#adding two series

s1 = pd.Series(12,index=[1,2,3,4,5,6,7])
ss = pd.Series(12,index=[1,2,3,4])

#prints upto 4 indixes then gives NaN ,gives broadcast error in numpy.
print("example 4")
print(s1+ss)
print('\n' * 5)


#learning about data structures in pandas 
#2 DataFrame(2-D data)

#basic examples on data frames

import pandas as pd

l=[1,2,3,4,5]
var= pd.DataFrame(l)
print(type(var))
print("\n"*5)

#data frame from dictionary

#length of data should be same for dataframe
d = {"a":[1,2,3,4,5], "b":[1,2,3,4,5,],"c":[1,2,3,4,5],1:[1,2,3,4,5]}
var1 = pd.DataFrame(d, columns=['a',1],index=["1.","2.","3.","4.","5."])
print(var1)
print("\n"*5)

#accessing a value from data frame

d = {"a":[1,2,3,4,5], "b":[11,21,31,41,51,],"c":[12,22,32,42,52],1:[13,23,33,43,53]}
var1 = pd.DataFrame(d)
print(var1)
print(var1["b"][3])
print("\n"*5)


#dataframe from list of list

list1 = [[1,2,3,4,5],[11,12,3,14,15]]
var2 = pd.DataFrame(list1)
print(type(var2))
print(var2)
print("\n"*5)

#dataframe from series

siri ={"s":pd.Series([1,2,3,4,]),"r":pd.Series([11,12,13,14])}
var3 = pd.DataFrame(siri)
print(type(var3))
print(var3)
print("\n"*5)

###
# DELETE AND INSERT FUNCTION IN PANDAS
###
print("DELETE AND INSERT FUNCTION IN PANDAS")
print("\n")


inst = pd.DataFrame({"A": [1,2,3,4,5],"B":[11,12,13,14,15]})
 
 # var.insert(position ,name , values)

inst.insert(1,"X",["1X","2X","3X","4X","5X"])
print(inst)
print("\n")

#slicing

sli = pd.DataFrame({"A": [1,2,3,4,5],"B":[11,12,13,14,15]})
sli["slicedA"] = sli["A"][:5:2]
print(sli)
print("\n")

#delet (by pop )

dell = pd.DataFrame({"A": [1,2,3,4,5],"B":[11,12,13,14,15],"C": [1,2,3,4,5]})
print(dell)
print("\n")
dell1 = dell.pop("B")
print(dell)
print("\n")
print(dell1)