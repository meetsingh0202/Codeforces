nums=input().split("+")
nums.sort()
str1=""
for i in nums:
    str1=str1+i+"+"
print(str1[:-1])