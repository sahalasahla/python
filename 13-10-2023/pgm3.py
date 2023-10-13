dict1={1:10,2:20}
dict2={2:25,4:35}
dict3={}
for d in (dict1,dict2):dict3.update(d)
print(dict3)
