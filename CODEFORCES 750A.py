numberofproblems,totaltime=map(int,input().split())
maximumtime=240
totaltimespent=0
timespentonquestions=0
c=0
for i in range(1,numberofproblems+1):
    timespentonquestions+=i*5
    if timespentonquestions+totaltime<=maximumtime:
        c+=1
        totaltimespent=timespentonquestions+totaltime
print(c)
