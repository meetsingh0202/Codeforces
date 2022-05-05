n=int(input())
arr=[]
for i in range(n):
    list1=list(map(int,input().split()))
    arr.append(list1)
max1=0
x1=0
for i in arr:
    x1=x1-i[0]+i[1]
    if max1<x1:
        max1=x1
print(max1)