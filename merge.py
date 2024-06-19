import pandas as pd

var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2 = pd.DataFrame({"A":[1,2,4,5],"c":[111,112,113,114]})

print(pd.merge(var1, var2 , on="A")) # merges only common data from both data frame 

print("\n")

print(pd.merge(var1,var2,how="inner")) # MERGES COMPLETE DATA ONLY
print("\n")
print(pd.merge(var1,var2,how="right")) #MERGES WITH VARIABLE ON RIGHT
print("\n")
print(pd.merge(var1,var2,how="left")) #MERGES WITH VARIABLE ON LEFT
print("\n")
print(pd.merge(var1,var2,how="outer",indicator=True)) #MERGES BOTH COMPLETLY
print("\n")

print(pd.merge(var1,var2,left_index=True,right_index=True))
print("\n")
### CONCAT 

sr1 = pd.Series([1,2,3,4])
sr2 = pd.Series([11,12,13,14])

vr1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
vr2 = pd.DataFrame({"A":[1,2,5],"c":[111,113,114]})

print(pd.concat([sr1,sr2]))
print("\n")
print(pd.concat([vr1,vr2]))
print("\n")

#Various parameters
print(pd.concat([vr1,vr2],axis=1,join="inner"))
print("\n")

print(pd.concat([vr1,vr2],axis=1,join="outer"))
print("\n")

v1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
v2 = pd.DataFrame({"A":[1,2,5,6],"c":[111,113,114,116]})

print(pd.concat([v1,v2],axis=1,keys=["v1","v2"]))
print("\n")

print(pd.concat([v1,v2],axis=0,keys=["v1","v2"]))
print("\n")

###
#The primary difference between merge and concat in Pandas is how the dataframes are combined.
#Concat function concatenates dataframes along rows or columns. It is similar to stacking up multiple dataframes. Merge function combines dataframes based on values in shared columns.
#Merge offers more flexibility compared to concat because it allows combinations based on a condition.



