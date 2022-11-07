for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    sum1 = sum(l1)
    sum2 = sum(l2)
    print(sum1 + sum2 - max(l2))