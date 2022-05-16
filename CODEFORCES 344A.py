n=int(input())
list1=[]
x=input()
c=0
for _ in range(1,n):
    x1=input()
    if x[0]!=x1[0]:
        c+=1
    x=x1
print(c+1)
