from collections import Counter

def solution(s):
    s = (s.replace("{", "").replace("}", "").split(","))
    count = Counter(s)
    return [int(x[0]) for x in count.most_common()]