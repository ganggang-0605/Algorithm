import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [[] for _ in range(n + 1)]
distance = [sys.maxsize] * (n + 1)

for _ in range(m):
    start, end, weight = map(int, input().split())
    lst[start].append((end, weight))

def Dijkstra(start, end):
    queue = PriorityQueue()
    queue.put((0, start))
    distance[start] = 0
    while not queue.empty():
        current_dist, temp = queue.get()

        if temp == end:
            return current_dist
        
        if distance[temp] < current_dist:
            continue

        for next_node, weight in lst[temp]:
            cost = current_dist + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                queue.put((cost, next_node))

s, e = map(int, input().split())
print(Dijkstra(s, e))