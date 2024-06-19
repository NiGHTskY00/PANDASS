#GROUPBY #IMP DOR   

import pandas as pd

var = pd.DataFrame({"name": ["Q","A","A","r","t","A","z","r","Q","Q"],"S_1": [1,2,3,4,5,6,7,8,8,10],"S_2": [11,21,31,41,51,61,71,81,81,101]})
print(var)

print("\n")

var_grouped = var.groupby("name")
print(var_grouped)

for x,y in var_grouped:
    print(x)
    print(y)
    print("\n")

# to access a particular group

print(var_grouped.get_group("Q"))
print("\n")


# applying maths

print(var_grouped.min())
print("\n")

print(var_grouped.max())
print("\n")

print(var_grouped.mean())
print("\n")


#converting data frame to list

li = list(var_grouped)
print(li)
print("\n")

#JOIN

import pandas as pd

varR1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
varR2 = pd.DataFrame({"C":[10,20,30,40], "D":[21,22,23,24]})

print(varR1.join(varR2))

print("\n")

# TO CHANGE INDEX YOU SHOULD PROVIDE SAME INDEX TO BOTH
# HOW ATTRIBUTE WORKS IN THIS FUNCTION



###  MELT - coverts the table into a verticle table
marks = pd.DataFrame({"D":[1,2,3,4,5,6], "MATH":[11,12,13,14,15,16],"ENGLISH":[11,21,13,64,15,61]})
print(marks)
print("\n")

print(pd.melt(marks))
print("\n")

print(pd.melt(marks,id_vars=["D"]))
print("\n")

### PIVOT 
mark = pd.DataFrame({"D":[1,2,3,4,5,6],"STUDENTS":["ROHAN","RAHIL","RITIK","RITI","RUTU","REXY"] ,"MATH":[11,12,13,14,15,16],"ENGLISH":[11,21,13,64,15,61]})
print(mark)
print("\n")

print(mark.pivot(index="D",columns="STUDENTS"))
print("\n")

# ATTRIBUTES
#aggfunc for applying mathematics
#margin gives average value
