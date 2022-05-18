sum1,sum2,sum3,sum4=map(int,input().split())
list1=[sum1,sum2,sum3,sum4]
list1.sort()
res=[]
totalsum=list1[3]
for i in range(3):
    x=totalsum-list1[i]
    res.append(x)
print(*res)
