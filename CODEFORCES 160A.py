n=int(input())
arr=list(map(int,input().split()))
totalsum=sum(arr)
arr.sort(reverse=True)
x=0
for i in range(len(arr)):
    x+=arr[i]
    y=totalsum-x
    if x>y:
        print(i+1)
        break