#1
"""for i in range (1,num+1):
    print("*"*i)"""
#2
"""for i in range (num,0,-1):
    print("*"*i)"""
#4
"""for i in range (num,0,-1):
    print(" "*(num-i)+"*"*i)"""
#5
"""for i in range (1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()"""
#6
"""x=1
for i in range(1,num+1):
    for j in range (1,i):
        print(x,end="")
        x+=1
        if(x==10):
            x=1
    print()"""
#7
x=65    
"""for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(x),end="")
        x+=1
    print()"""
#8
"""for i in range(1,num+1):
    print(" "*(num-i)+"*"*(2*i-1))"""
#11
"""for i in range(1,num+1):
    print(" "*(num-i)+"*"*(2*i-1))
for i in range(num-1,0,-1):
    print(" "*(num-i)+"*"*(2*i-1))"""
#9
"""for i in range (1,num+1):
    print(" "*(num-i)+"*"*i+" "*(num+1-i)+"*"*i)"""
#10
"""for i in range (1,num+1):
    for j in range (1,num+1):
        if(i==1 or j==1 or j==num or i==num):
            print("*",end="")
        else:
            print(" ",end="")
    print() """
