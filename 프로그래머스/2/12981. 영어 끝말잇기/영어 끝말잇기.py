def solution(n, words):
    lst = []
    answer = [0, 0]
    for i in range(len(words)):
        num, seq = (i % n) + 1, (i // n) + 1
        # print(num, seq)
        now = words[i]
        if i != 0:
            if now in lst or words[i][0] != words[i-1][-1]:
                answer = [num, seq]
                break
        lst.append(words[i])

    return answer