import sys
input = sys.stdin.readline

lst = []
for _ in range(5):
    lst.append(list(map(int, input().split())))

sequence = []
for i in range(0, 25, 5):
    sequence[i:i+5] = list(map(int, input().split()))

for k in range(25):
    bingo = 0
    for i in range(5):
        for j in range(5):
            if lst[i][j] == sequence[k]:
                lst[i][j] = 0

    for r in range(5):
        if lst[r] == [0, 0, 0, 0, 0]:
            bingo += 1
    for c in range(5):
        if [row[c] for row in lst] == [0, 0, 0, 0, 0]:
            bingo += 1
    if [lst[i][i] for i in range(5)] == [0, 0, 0, 0, 0]:
        bingo += 1
    if [lst[i][5 - 1 - i] for i in range(5)] == [0, 0, 0, 0, 0]:
        bingo += 1
    
    if bingo >= 3:
        print(k + 1)
        break