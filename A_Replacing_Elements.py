for _ in range(int(input())):
    n,d=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    if arr[0]+arr[1]<=d or arr[-1]<=d:
        print("YES")
    else:
        print("NO")