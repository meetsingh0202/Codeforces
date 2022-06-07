for _ in range(int(input())):
    str1=input()
    flag=True
    for i in range(len(str1)):
        if (i==0 or str1[i]!=str1[i-1]) and (i==len(str1)-1 or str1[i]!=str1[i+1]):
            flag=False
    if flag==True:
        print("YES")
    else:
        print("NO")