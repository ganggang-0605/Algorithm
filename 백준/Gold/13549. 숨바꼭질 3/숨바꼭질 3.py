import sys
from queue import PriorityQueue
input = sys.stdin.readline

n, k = map(int, input().split())
queue = PriorityQueue()
queue.put((0, k))

INF = float('inf')
visited = [INF] * 100001
visited[k] = 0

while queue.qsize() > 0:
    time, temp = queue.get()
    
    if time > visited[temp]:
        continue

    if temp == n:
        print(time)
        break

    if temp % 2 == 0 and time < visited[temp // 2]:
        visited[temp // 2] = time
        queue.put((time, temp // 2))
    if temp - 1 >= 0 and time + 1 < visited[temp - 1]:
        visited[temp - 1] = time + 1
        queue.put((time + 1, temp - 1))
    if temp + 1 <= 100000 and time + 1 < visited[temp + 1]:
        visited[temp + 1] = time + 1
        queue.put((time + 1, temp + 1))