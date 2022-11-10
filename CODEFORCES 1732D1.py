n = int(input())
HashSet = set()
HashMap = dict()
for i in range(n):
    operator, num = map(str, input().split())
    if operator == '+':
        HashSet.add(int(num))
    else:
        num = int(num)
        if num not in HashMap:
            HashMap[num] = num
        while HashMap[num] in HashSet:
            HashMap[num] += num
        print(HashMap[num])
