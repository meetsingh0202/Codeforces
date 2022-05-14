str1=input()
l=["H","Q","9"]
c=0
for i in str1:
    if i in l:
        print("YES")
        c=1
        break
if c==0:
    print("NO")