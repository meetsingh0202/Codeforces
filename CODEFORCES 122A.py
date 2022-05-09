n=int(input())
lucky=[4,7,47,44,77,74,447,477,774,747,744,444,777,474]
flag=False
for i in lucky:
    if n%i==0:
        print("YES")
        flag=True
        break
if flag==False:
    print("NO")