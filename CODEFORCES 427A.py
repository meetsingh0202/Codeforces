n=int(input())
arr=list(map(int,input().split()))
flag=False
c=0
countofpolicemen=0
for i in arr:
    if flag==True and i>0:
        countofpolicemen+=i
    elif flag==False and i<0:
        c+=1
    elif flag==False and i>0:
        countofpolicemen+=i
        flag=True
    elif flag==True and i<0:
        if countofpolicemen>0:
            countofpolicemen-=abs(i)
            if countofpolicemen<=0:
                flag=False
        else:
            c+=1
            flag=False
print(c)
