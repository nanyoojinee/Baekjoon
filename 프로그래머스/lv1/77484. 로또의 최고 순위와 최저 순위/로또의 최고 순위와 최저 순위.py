def solution(lottos, win_nums):
    answer = []
    num=0
    numzero=0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            num+=1
        elif lottos[i]==0:
            numzero+=1
    if num+numzero==6:
        answer.append(1)
    elif num+numzero==5:
        answer.append(2)
    elif num+numzero==4:
        answer.append(3)
    elif num+numzero==3:
        answer.append(4)
    elif num+numzero==2:
        answer.append(5)
    else:
        answer.append(6)
        
    if num==6:
        answer.append(1)
    elif num==5:
        answer.append(2)
    elif num==4:
        answer.append(3)
    elif num==3:
        answer.append(4)
    elif num==2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer