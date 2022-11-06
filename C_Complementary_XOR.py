import os.path
from math import gcd, floor, ceil
from collections import *
import sys

mod = 1000000007
INF = float("inf")

def swap(a,b):
    temp=a
    a=b
    b=temp

def nCr(n, r):
    return (fact(n) / (fact(r)
                       * fact(n - r)))

def fact(n):
    res = 1

    for i in range(2, n + 1):
        res = res * i

    return res

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    ans = []
    for p in range(2, n + 1):
        if prime[p]:
            ans.append(p)
    return ans


def nextPowerOf2(n):
    count = 0
    if (n and not (n & (n - 1))):
        return n

    while (n != 0):
        n >>= 1
        count += 1

    return 1 << count


from collections import defaultdict


def primeFactors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            res.append(i)
            n = n // i
    if n > 2:
        res.append(n)
    return res


def upper_bound(arr, target):
    start = 0
    end = len(arr) - 1

    ans = -1
    while (start <= end):
        mid = (start + end) // 2

        # Move to right side if target is
        # greater.
        if (arr[mid] <= target):
            start = mid + 1

        # Move left side.
        else:
            ans = mid
            end = mid - 1

    return ans

def st():
    return list(sys.stdin.readline().strip())

def printDivisors(n):
    # Note that this loop runs till square root
    i = 1
    res = []
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                res.append(i)
            else:
                # Otherwise print both
                res.append(i)
                res.append(n // i)
        i = i + 1
    return res

def li():
    return list(map(int, sys.stdin.readline().split()))


def mp():
    return map(int, sys.stdin.readline().split())


def inp():
    return int(sys.stdin.readline())


def pr(n):
    return sys.stdout.write(str(n) + "\n")


def prl(n):
    return sys.stdout.write(str(n) + " ")


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def solve():
    n = int(input())
    x = input()
    y = input()
    x = [int(i) for i in x]
    y = [int(i) for i in y]
    # print(x, y)
    arr = []
    r = []
    temp = [0] * n
    flag = 0
    count1 = 0
    for i in range(len(x)):
        a = int(x[i])
        if a == 1:
            count1 += 1
            temp[i] -= 1
            r.append([i + 1, i + 1])
    
    for i in range(n):
        if (temp[i] + count1) % 2 == 1:
            if y[i] == 1:
                y[i] = 0
            else:
                y[i] = 1

    tempChar = y[0]

    for i in range(n):
        if y[i] != tempChar:
            print('NO')
            return
    print("YES")
    if tempChar == 0:
        print(len(r))
        for i in range(len(r)):
            print(*r[i])
    else:
        if n > 2:
            HashMap = defaultdict(int)
            # print(len(r) + 5)
            # for i in range(len(r)):
            #     print(*r[i])
                # set.add((r[i][0], r[i][1]))
            r.append((n, n))
            r.append((1, 1))
            r.append((2, n - 1))
            r.append((1, 1))
            r.append((2, n))
            count = 0
            temp1 = []
            for i in r:
                HashMap[tuple(i)] += 1
            for key, val in HashMap.items():
                if val % 2 == 1:
                    count += 1
                    temp1.append((min(key[0], key[1]), max(key[0], key[1])))
            print(count)
            for i in temp1:
                print(i[0], i[1])
        else:
            HashMap = defaultdict(int)
            count = 0
            temp1 = []
            r.append([1, 1])
            r.append([2, 1])
            r.append([2, 2])
            temp1 = []
            for i in r:
                HashMap[tuple(i)] += 1
            for key, val in HashMap.items():
                if val % 2 == 1:
                    count += 1
                    temp1.append((min(key[0], key[1]), max(key[0], key[1])))
            print(count)
            for i in temp1:
                print(i[0], i[1])

def solve1():
    n = int(input())
    x = input()
    y = input()
    x = [int(i) for i in x]
    y = [int(i) for i in y]
    r = [[], []]
    dp = [0] * n
    for i in range(n):
        index = i
        while i < n and x[i] == 1:
            i += 1
        if index != i:
            r[0].append(index + 1)
            r[1].append(i)
            dp[0] += 1
            dp[index] -= 1
            try:
                dp[i] += 1
            except:
                pass
    p = 0
    temp = 0
    res = [0] * n
    for i in range(n):
        temp += dp[i]
        if (y[i] == 0 and temp % 2 == 1) or (y[i] == 1 and temp % 2 ==0):
            res[i] = 1
        else:
            res[i] = 0
    for i in range(n - 1):
        if res[i] != res[i + 1]:
            p = 1
    if p == 0:
        print("YES")
        if res[0] == 1:
            r[0].append(1)
            r[1].append(n)
            r[0].append(1)
            r[1].append(1)
            r[0].append(2)
            r[1].append(n)
        print(len(r[0]))
        for i in range(len(r[0])):
            print(r[0][i], r[1][i])
    else:
        print("NO")
    
num_test = 1
num_test = int(input())
# print(num_test)
for _ in range(num_test):
    solve()