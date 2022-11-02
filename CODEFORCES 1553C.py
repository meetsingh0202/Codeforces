t = int(input())
for _ in range(t):
    s = input()
    t1, t2, w1, w2 = 0, 0, 0, 0
    for i in range(len(s)):
        if i % 2:
            if s[i] == '1':
                t2 += 1
            elif s[i] == '?':
                w2 += 1
        else:
            if s[i] == '1':
                t1 += 1
            elif s[i] == '?':
                w1 += 1
        if t2 + (10 - i) // 2 < t1 + w1 or t1 + (9 - i) // 2 < t2 + w2:
            print(i + 1)
            break
    else:
        print(10)
