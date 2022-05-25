num1=int(input("enter the side of triangle:"))
num2=int(input("enter the side of triangle:"))
num3=int(input("enter the side of triangle:"))
if((num1+num2)>num3 or (num1+num3)>num2 or (num2+num3)>num1):
    print("the triangle is possible!")
else:
    print("the triangle is not possible!")
