k,n,w=map(int,input().split())
totalcost=0

for i in range(1,w+1):
    totalcost+=i*k
print(totalcost-n)