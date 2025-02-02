from itertools import combinations
def solution(friends, gifts):
    gift_dict = {}
    for friend in friends:
        gift_dict[friend] = {
            friend: 0 for friend in friends
        }
        
    gift_score = { friend: 0 for friend in friends }
    
    for gift in gifts:
        gift_from, gift_to = tuple(gift.split())
        gift_dict[gift_from][gift_to] += 1
        gift_score[gift_from] += 1
        gift_score[gift_to] -= 1
        
    gift_to_get = { friend: 0 for friend in friends }
        
    for a, b in combinations(friends, 2):
        if gift_dict[a][b] > gift_dict[b][a]:
            gift_to_get[a] += 1
        elif gift_dict[a][b] < gift_dict[b][a]:
            gift_to_get[b] += 1
        elif gift_score[a] > gift_score[b]: 
            gift_to_get[a] += 1
        elif gift_score[a] < gift_score[b]: 
            gift_to_get[b] += 1
    
    return max(gift_to_get.values())