a,b=map(int,input().split())
c=0
while True:
    c+=1
    a=a*3
    b=b*2
    if a>b:
        print(c)
        break