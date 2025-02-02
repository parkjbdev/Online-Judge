from collections import defaultdict
def solution(survey, choices):
    rcja = defaultdict(int)
    answer = 'RCJA'
    
    for question, choice in zip(survey, choices):
        choice -= 4
        if question[0] in answer: choice = -choice
        else: question = question[::-1]
        rcja[question[0]] += choice
        
    if rcja['R'] < 0: answer = answer.replace('R', 'T')
    if rcja['C'] < 0: answer = answer.replace('C', 'F')
    if rcja['J'] < 0: answer = answer.replace('J', 'M')
    if rcja['A'] < 0: answer = answer.replace('A', 'N')
    
    return answer