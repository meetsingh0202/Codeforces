for _ in range(int(input())):
   n=int(input())
   s=input()
   if s[0]!='9':
       print(int('9'*n)-int(s))
   else:
       print(int('1'*(n+1))-int(s))