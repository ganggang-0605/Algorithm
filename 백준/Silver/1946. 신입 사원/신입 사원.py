import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    scores = []
    for _ in range(n):
        scores.append(list(map(int, input().split())))
    scores.sort()

    cnt = 1
    temp = scores[0][1]
    tempIdx = 0
    for i in range(n):
        if scores[i][1] < temp:
            cnt += 1
            tempIdx = i
            temp = scores[i][1]

    print(cnt)
