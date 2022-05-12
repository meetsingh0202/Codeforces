x=input()
y=input()
res=""
for i in range(len(x)):
    if x[i]==y[i]:
        res=res+'0'
    else:
        res=res+'1'
print(res)