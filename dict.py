dict={}
x=int(input())
for i in range(x):
    k=int(input())
    v=int(input())
    dict.update({k:v})
print(dict)
d3={}
dict1={}
x1=int(input())
for i in range(x1):
    k1=int(input())
    v1=int(input())
    dict1.update({k1:v1})
print(dict1)
print(dict.values())
print(dict.keys())
print(dict.items())
print(sum(dict.values()))
print(sorted(dict.values()))
for i in (dict,dict1):
    d3.update(i)
print(d3)
