str1=input()
l1='abcdefghijklmnopqrstuvwxyz'
l2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c1=0
c2=0
for i in str1:
    if i in l1:
        c1+=1
    if i in l2:
        c2+=1
if c1>=c2:
    str1=str1.lower()
else:
    str1=str1.upper()
print(str1)