x,y=map(int,input().split())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i>y:
        l.append(2)
    else:
        l.append(1)
print(sum(l))