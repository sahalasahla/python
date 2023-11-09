n=input("Enter a string")
if(n[-3: ]=="ing"):
    n=n[:-3]+"ly"
else:
    n=n[ : ]+"ing"
print(n)
