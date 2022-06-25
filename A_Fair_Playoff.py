for t in range(int(input())):
	a,b,c,d = map(int,input().split())
	if max(a,b)<min(c,d) or min(a,b)>max(c,d):
		print("NO")
	else:
		print("YES")