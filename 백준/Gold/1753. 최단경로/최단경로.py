import sys
from queue import PriorityQueue

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())

lst = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    start, end, weight = map(int, input().split())
    lst[start].append((end, weight))

def Dijkstra(start):
    distance[start] = 0
    queue = PriorityQueue()
    
    queue.put((0, start))

    while not queue.empty():
        current_dist, temp = queue.get()

        if distance[temp] < current_dist:
            continue

        for next_node, weight in lst[temp]:
            cost = current_dist + weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                queue.put((cost, next_node))

Dijkstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])