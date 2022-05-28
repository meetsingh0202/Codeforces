for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    c=0
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]>1:
            print("NO")
            c=1
            break
    if c==0:
        print("YES")