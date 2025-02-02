import sys
from collections import defaultdict, deque
from itertools import combinations

graph = defaultdict(list)

def is_adjacent(word1, word2):
    # return sum(x != y for x, y in zip(word1, word2))
    res = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2: res+=1
        if res > 1: return False
        
    return True 

def solution(begin, target, words):
    if target not in words: return 0
    
    global graph
    
    for word1, word2 in combinations(words + [begin], 2):
        if is_adjacent(word1, word2):
            graph[word1].append(word2)
            graph[word2].append(word1)
    
    dq = deque()
    visited = {k: False for k, v in graph.items()}
    visited[begin] = True
    level = 0
    dq.append((begin, level))
    
    while len(dq) != 0:
        current_word, current_level = dq.popleft()
        
        for next_word in graph[current_word]:
            if not visited[next_word]:
                visited[next_word] = True
                dq.append((next_word, current_level + 1))
                if next_word == target: return current_level + 1
                
    return 1
