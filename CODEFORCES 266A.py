n=int(input())
str1=input()
c=0
for i in range(1,len(str1)):
    if str1[i]==str1[i-1]:
        c=c+1
print(c)