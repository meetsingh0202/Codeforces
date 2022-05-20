for _ in range(int(input())):
    def sum1(x):
        sum1=0
        for i in x:
            sum1+=int(i)
        return sum1
    str1=input()
    x=str1[:3]
    y=str1[-3:]
    x1=sum1(x)
    y1=sum1(y)
    if x1==y1:
        print("YES")
    else:
        print("NO")