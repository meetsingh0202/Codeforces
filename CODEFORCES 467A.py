n=int(input())
list1=[]
c=0
for i in range(n):
    x,y=map(int,input().split())
    if y-x>=2:
        c+=1
print(c)
