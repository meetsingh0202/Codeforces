str1=input()
dict1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
res=0
curr=0
for i in str1:
    required=dict1.index(i)
    work=abs(required-curr)
    work1=abs(work-26)
    res+=(min(work,work1))
    if work<0:
        work=work+26
    curr=required
print(res)