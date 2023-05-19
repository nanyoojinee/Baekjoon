def solution(array, commands):
    answer = []
    for i in commands:
        newarray=array[i[0]-1:i[1]]
        newarray.sort()
        answer.append(newarray[i[2]-1])

    return answer