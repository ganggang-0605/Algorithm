def solution(s):
    new = s.split(' ')
    answer = []
    for temp in new:
        if temp == "":
            answer.append("")
            continue

        modified = ""
        for i in range(len(temp)):
            if i == 0:
                if 'a' <= temp[i] <= 'z':
                    modified += temp[i].upper()
                else:
                    modified += temp[i]
            else:
                if 'A' <= temp[i] <= 'Z':
                    modified += temp[i].lower()
                else:
                    modified += temp[i]

        answer.append(modified)
    return ' '.join(answer)