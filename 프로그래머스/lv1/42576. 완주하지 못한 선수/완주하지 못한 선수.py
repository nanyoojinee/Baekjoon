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
    participant.sort()
    completion.sort()
   
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            break
    return participant[-1]