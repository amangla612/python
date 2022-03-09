a=int(input('Enter a number to check ARMSTRONG :'))
sum=0
copy=a
while(a>0):
    temp=a%10
    cube=temp*temp*temp
    sum=sum+cube
    a=a//10
if(sum==copy):
    print('Yes it is armstrong number')
else:
    print('No it is not armstrong number')
