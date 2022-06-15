import math
a,b,n=map(int,input().split())

while n!=0:
    x=math.gcd(a,n)
    n=n-x
    if n==0:
        print(0)
        break
    y=math.gcd(b,n)
    n=n-y
    if n==0:
        print(1)
        break