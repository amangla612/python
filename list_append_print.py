lst1=list(map(int,input().split()))
lst4=[]
for i in lst1:
    if i not in lst4:
        lst4.append(i)
lst2=list(map(int,input().split()))
lst5=[]
for i in lst2:
    if i not in lst5:
        lst5.append(i)
lst3=list(filter(lambda n: n in lst1,lst2))
print(lst3)
