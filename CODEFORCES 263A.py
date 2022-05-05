arr=[]
for i in range(5):
    list1=list(map(int,input().split()))
    arr.append(list1)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==1:
            index=(i,j)
middle=(2,2)
diff=abs(index[0]-middle[0])+abs(index[1]-middle[1])
print(diff)