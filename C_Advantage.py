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
    arr = li()
    Max = max(arr)
    tempArr = arr[:]
    tempArr.remove(Max)
    SecondMax = max(tempArr)
    res = []
    for i in arr:
        if i != Max:
            res.append(i - Max)
        else:
            res.append(Max - SecondMax)
    print(*res)

    
num_test = 1
num_test = int(input())
# print(num_test)
for _ in range(num_test):
    solve()