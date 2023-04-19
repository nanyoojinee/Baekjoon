a,n = map(int,input().split())
c = list(map(int,input().split()))
#n의 숫자를 넘지 않게 c리스트에서 3개 뽑기
t=0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if c[i]+c[j]+c[k]>t and c[i]+c[j]+c[k]<=n:
                t=c[i]+c[j]+c[k]
               
print(t)