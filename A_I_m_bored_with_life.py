x,y=map(int,input().split())
min1=min(x,y)
f=1
while min1>0:
    f*=min1
    min1-=1
print(f)