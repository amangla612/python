n=int(input("enter a no"))
if n>1:
    for x in range(2,int(n/2)+1):
        if(n%x==0):
            print("not a prime no")
            break
        else:
            print("prime no")
else:
    print("not a prime no")
