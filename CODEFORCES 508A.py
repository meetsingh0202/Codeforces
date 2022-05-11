n=int(input())
arr=list(map(int,input().split()))
c=0
max1=-1231
for i in range(len(arr)-1):
    if arr[i+1]>arr[i] or arr[i+1]==arr[i]:
        c+=1
    else:
        max1=max(max1,c)
        c=0
print(max(max1,c)+1)