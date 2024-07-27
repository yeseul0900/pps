def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        use_skills = ""
        for j in range(len(i)):
            if i[j] in skill:
                use_skills += i[j]
        if use_skills == skill[:len(use_skills)]:
            answer += 1
    return answer