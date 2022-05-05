n=int(input())
list1=[]
c=0
for _ in range(n):
    x,y,z=map(int,input().split())
    list1.append([x,y,z])
for i in list1:
    x,y,z=i[0],i[1],i[2]
    if x+y+z>1:
        c+=1
print(c)