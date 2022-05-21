for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    oddindices=[]
    evenindices=[]
    notplacedeven=[]
    notplacedodd=[]
    for i in range(len(arr)):
        if i%2==0:
            evenindices.append(arr[i])
        else:
            oddindices.append(arr[i])
        if arr[i]%2==0 and i%2!=0:
            notplacedeven.append(arr[i])
        elif arr[i]%2!=0 and i%2==0:
            notplacedodd.append(arr[i])
    if len(notplacedeven)!=len(notplacedodd):
        print(-1)
    else:
        print(len(notplacedeven))