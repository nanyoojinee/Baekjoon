count,num=map(int,input().split())
numlist=[]
for i in range(count):
    a = int(input())
    numlist.append(a)
newnum=0
t=0
for i in range(count):
    if newnum != num:
        newnum=numlist[newnum]
        t+=1
    else:
        print(t)
        break
else:
    print(-1)