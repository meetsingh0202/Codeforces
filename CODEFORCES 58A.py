str1=input()
str2="hello"
x=0
y=0
for i in range(len(str1)):
    if str1[i]==str2[x]:
        x+=1
        y+=1
        if y==5:
            break
if y==5:
    print("YES")
else:
    print("NO")