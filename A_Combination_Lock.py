n=int(input())
originalstate=input()
password=input()
res=0
for i in range(len(originalstate)):
    res+=min(10-abs(int(originalstate[i])-int(password[i])),abs(int(originalstate[i])-int(password[i])))
print(res)
    