x,y,z=map(int,input().split())
x2=x//z
if x%z!=0:
    x2+=1
x1=y//z
if y%z!=0:
    x1+=1
print(x2*x1)