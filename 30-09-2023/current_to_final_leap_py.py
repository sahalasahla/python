cur=int(input("Enter the current year:"))
final=int(input("Enter the final year"))
if cur < final:
    print("Enter the list of leap years between",cur,"to",final)
while cur<final:
    if(cur%4==0) and (cur%100!=0):
        print(cur)
    if(cur%100==0) and (cur%400==0):
        print(year," is leap year")
    cur=cur+1
if(cur>=final):
   print("check leap year again")


    
