arr1=[3,34,4,12,5,2]
arr=[3,34,4,12,5,32]
print(arr)
flag=False
i=0
j=1
tempsum=arr[i]
sum1=12
res=[]
n=len(arr)
dp=[[-1 for _ in range(n+1)]for _ in range(sum1+1)]
def check(arr,n,sum1):
    if sum1==0:
        return 1
    if n==0:
        return 0
    if dp[n][sum1]!=-1:
        return dp[n][sum1]
    if arr[n-1]>sum1:
        dp[n][sum]=check(arr,n-1,sum1)
        return dp[n][sum]
    else:
        dp[n][sum]=check(arr,n-1,sum1)
        dp[n][sum]=check(arr,n-1,sum1-arr[n-1])
        return dp[n][sum]
flag=check(arr,n,sum1)
print(flag)