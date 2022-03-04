n=int(input("enter a no:"))
p=n%10
while(n>=10):
    n=n//10
print("the sum of 1st and last digit is ",p+n)
