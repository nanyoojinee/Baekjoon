def solution(nums):
    answer = 0
    setnums= list(set(nums))
    answer= min(len(setnums),len(nums)/2)
    return answer