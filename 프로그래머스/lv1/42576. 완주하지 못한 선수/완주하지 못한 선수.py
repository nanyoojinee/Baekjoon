# def solution(participant, completion):
#     for n in range(len(participant)):
#         for i in participant: 
#             if i in completion:
#                 participant.remove(i)
#                 completion.remove(i)
#     return  participant[0]

# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     return participant[0]

# def solution(participant, completion):
#     parset=set(participant)
#     comset=set(completion)
#     answer=parset-comset
    
#     if len(answer) == 0:
#         return None
#     return list(answer)[0]

def solution(participant, completion):
    # 참가자 리스트를 정렬
    participant.sort()
    # 완주자 리스트를 정렬
    completion.sort()
    
    # 두 리스트를 비교하여 완주하지 못한 선수 찾기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 모든 완주자를 제외한 마지막 선수가 완주하지 못한 선수임
    return participant[-1]