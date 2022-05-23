arr=[0]
for i in range(1,10000):
    if i%3==0:
        continue
    x=str(i)
    if x[-1]=='3':
        continue
    arr.append(i)
for _ in range(int(input())):
    n=int(input())
    print(arr[n])