for _ in range(int(input())):
    str1=input()
    length=len(str1)
    if length>10:
        str2=str1[0]+str(length-2)+str1[-1]
        print(str2)
    else:
        print(str1)