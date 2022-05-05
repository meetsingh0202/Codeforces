n=int(input())
res=[]
x=0
for i in range(n):
    res.append(input())
for i in res:
    if i[1]=="+":
        x+=1
    else:
        x-=1
print(x)