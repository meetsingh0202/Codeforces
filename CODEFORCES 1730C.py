for t in range(int(input())):
    s = input()
    m = s[-1]
    ans = []
    for i in reversed(s):
        m = min(i,m)
        if(i<=m):
            ans.append(i)
        else:
            ans.append(str(min(int(i)+1,9)))
 
    print("".join(sorted(ans))) 
