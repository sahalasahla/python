n=(input("Enter a string"))
print("The original string is",n)
k="$"
res=n[0]+n[1:].replace(n[0],k)
print("replaced string",(res))
