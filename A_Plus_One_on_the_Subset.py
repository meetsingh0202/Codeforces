for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    max1=max(arr)
    min1=min(arr)
    print(max1-min1)