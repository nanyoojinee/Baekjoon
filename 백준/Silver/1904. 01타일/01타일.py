n= int(input())
Table = [0 for i in range(n+1)]

if n==1:
    print(1)
elif n==2:
    print(2)
else:
    Table[1] = 1
    Table[2] = 2
    for i in range(3, n+1):
        Table[i] = (Table[i-2] + Table[i-1])%15746
    print(Table[n])