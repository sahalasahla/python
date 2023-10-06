list=["abc","dfg","sahala","sahla"]
count=0
a=str(input("letter to search:"))
for i in list:
    for f in i:
        if f=="a":
            count=count+1
print("count of",a,"in",list,"is:",count)
