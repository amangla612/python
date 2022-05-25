def reverse():
    rev=0
    sum=0
    num=int(input())
    temp=num
    while num>0:
        rem=num%10
        sum+=rem
        rev=10*rev+rem
        num//=10
    print(sum)
    if temp==rev:
        print('palindrome')
    else:
        print('not palindrome')
reverse()
