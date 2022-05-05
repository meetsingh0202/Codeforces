n=int(input())
str1=input()
a=0
d=0
for i in str1:
    if i=='A':
        a+=1
    else:
        d+=1

if a==d:
    print("Friendship")
elif d>a:
    print("Danik")
else:
    print("Anton")