n=int(input())
if n==1:
    print("I hate it")
else:
    dict1={1:"I hate",0:"I love"}
    str1=""
    for i in range(1,n+1):
        x=i%2
        str1=str1+dict1[x]
        if i==n:
            str1=str1+" it "
            continue
        str1=str1+' that '
    print(str1)