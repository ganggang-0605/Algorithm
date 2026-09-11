def solution(array, commands):
    answer = []
    for s, e, k in commands:
        lst = array[s-1:e]
        lst.sort()
        answer.append(lst[k-1])
    return answer