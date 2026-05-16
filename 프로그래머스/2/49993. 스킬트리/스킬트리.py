import re

def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):      
        now = "".join([s for s in skill_trees[i] if s in skill])
        if skill.startswith(now):
            answer += 1

    
    return answer