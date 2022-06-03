for _ in range(int(input())):
    n=int(input())
    cards=list(map(int,input().split()))
    m=int(input())
    shuffle=list(map(int,input().split()))
    sumofshuffles=sum(shuffle)
    #print(sumofshuffles)
    print(cards[sumofshuffles%n])