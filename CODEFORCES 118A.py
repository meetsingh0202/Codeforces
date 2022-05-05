str1=input()
vowel=['a','e','i','o','u','A','E','I','O','U','Y','y']
res=""
for i in str1:
    if i not in vowel:
        res=res+"."+i.lower()
print(res)