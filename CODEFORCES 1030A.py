n=int(input())
arr=list(map(int,input().split()))
x=sum(arr)
if x>0:
    print("HARD")
else:
    print("EASY")