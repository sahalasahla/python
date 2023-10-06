a=int(input('Enter the limit:'))
i=0
ls=[]
while i<a:
    z=int(input("Enter the number"))
    if z>100:
        ls.append("over")
    else:
         ls.append(z)
    i+=1
print(ls)
