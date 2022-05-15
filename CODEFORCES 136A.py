n=int(input())
arr=list(map(int,input().split()))
list1=[0]*(n+1)

for index,value in enumerate(arr):
    list1[value]=index+1
list1.pop(0)
print(*list1)