for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    currSum = 0
    res = float('inf')
    for i in range(len(arr)):
        currSum += arr[i]
        nextStart = i + 1
        currCount = i + 1
        tempSum = 0
        tempCount = 0
        flag = True
        for j in range(nextStart, len(arr)):
            tempCount += 1
            tempSum += arr[j]
            currCount = max(currCount, tempCount)
            if tempSum == currSum:
                tempSum = 0
                tempCount = 0
            if tempSum >= currSum:
                flag = False
        if flag == True and tempSum == 0:
            res = min(res, currCount)
    print(res)
