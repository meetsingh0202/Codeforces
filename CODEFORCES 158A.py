x,y=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for index,value in enumerate(arr):
    if arr[y-1]<=value and value!=0:
        c+=1
print(c)