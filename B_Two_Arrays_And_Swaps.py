for _ in range(int(input())):
    n,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr1.sort()
    arr2.sort(reverse=True)
    j=0
    for i in range(k):
        if arr1[i]<arr2[j]:
            arr1[i]=arr2[j]
            j+=1
        else:
            break
    print(sum(arr1))