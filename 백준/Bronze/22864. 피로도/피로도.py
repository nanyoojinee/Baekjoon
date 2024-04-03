A, B, C, M = map(int, input().split())
work = 0
pirodo = 0
_time = 0
while _time < 24:
    if pirodo + A <= M:
        work += B
        pirodo += A
    else:
        pirodo -= C
        if pirodo < 0:
            pirodo = 0
    _time += 1

print(work)
