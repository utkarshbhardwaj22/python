import pandas as pd

numbes=[11,22,33,44,55]

s1=pd.Series(numbes)

print(s1)

ages={"john":20,"jennie":30,"jim":40,"jack":50,"joe":60}
s2=pd.Series(ages)

print(s2)

print(s1[0])

print()

print(s2["jennie"])
print()

print(s1[2:5])

print()

print(s2["jim":"joe"]) #jim and joe in inclusive

