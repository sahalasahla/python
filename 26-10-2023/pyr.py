n=int(input('Enter the number'))
def pyramid(n):
    for i in range(1,n+1):
        for n in range(1,i+1):
            print(n*i,end="")
        print("\n")
pyramid(n)
                
