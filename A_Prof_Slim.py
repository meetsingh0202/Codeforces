for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    x=arr[:]
    x.sort()
    if arr==x:
        print("YES")
    else:
        i=0
        j=len(arr)-1
        while i<len(arr) and j>0:
            if i>j:
                break
            if arr[i]>0 and arr[j]<0:
                arr[i]=arr[i]*-1
                arr[j]=arr[j]*-1
                i+=1
                j-=1
            elif arr[i]>0:
                j-=1
                continue
            elif arr[i]<0:
                i+=1
                continue
            else:
                print("NO")
                break
        if arr==sorted(arr):
            print("YES")
        else:
            print("NO")