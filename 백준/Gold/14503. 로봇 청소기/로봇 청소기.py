import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
lst = []

r, c, d = map(int, input().split())
for i in range(n):
    lst.append(list(map(int, input().split())))

cnt = 0
while True:
    if lst[r][c] == 0:
        lst[r][c] = -1
        cnt += 1

    flag = False

    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 0:
            r, c = nr, nc
            flag = True
            break

    if not flag:
        br, bc = r - dr[d], c - dc[d]

        if 0 <= br < n and 0 <= bc < m and lst[br][bc] == 1:
            break
        else:
            r, c = br, bc

print(cnt)