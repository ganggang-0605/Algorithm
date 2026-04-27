import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    a, b = map(int, input().split())
    queue = deque([(a, 1)])

    while queue:
        a, cnt = queue.popleft()
        # print(a)
        if a == b:
            return cnt

        if a * 2 <= b:
            queue.append((a * 2, cnt + 1))
        if int(str(a) + '1') <= b:
            queue.append((int(str(a) + '1'), cnt + 1))
    return -1

print(bfs())