n,initialcandies=map(int,input().split())
list1=[]
for i in range(n):
    list2=list(map(str,input().split()))
    list1.append(list2)
kidsleftdistress=0
curr=initialcandies
for i in list1:
    if i[0]=='+':
        curr+=int(i[1])
    elif i[0]=='-':
        if curr-int(i[1])>=0:
            curr-=int(i[1])
        else:
            kidsleftdistress+=1
   
print(curr,kidsleftdistress)