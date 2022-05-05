n=int(input())
mat=[]
for i in range(n):
    list1=list(map(int,input().split()))
    mat.append(list1)
print(mat)
sum1=0
for i in range(0,3):
    for j in range(n):
        sum1=sum1+mat[j][i]

if sum1==0:
    print("YES")
else:
    print("NO")