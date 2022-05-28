for _ in range(int(input())):
    hours,minutes=map(int,input().split())
    hourstominutes=hours*60
    totalminutes=minutes+hourstominutes
    res=1440-totalminutes
    print(res)