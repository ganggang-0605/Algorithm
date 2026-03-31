import sys
from queue import PriorityQueue
input = sys.stdin.readline

n, k = map(int, input().split())

queue = PriorityQueue()
queue.put((0, k))
visited = [False] * 100001
visited[k] = True

while queue.qsize() > 0:
    cnt, temp = queue.get()
    if temp == n:
        print(cnt)
        break
    
    if temp - 1 >= 0 and not visited[temp - 1]:
        queue.put((cnt + 1, temp - 1))
        visited[temp - 1] = True
    if temp + 1 <= 100000 and not visited[temp + 1]:
        queue.put((cnt + 1, temp + 1))
        visited[temp + 1] = True
    if temp % 2 == 0 and not visited[temp//2]:
        queue.put((cnt + 1, temp // 2))
        visited[temp // 2] = True