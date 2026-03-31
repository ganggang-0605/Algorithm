import sys
input = sys.stdin.readline

k, l = map(int, input().split())
waiting_dict = {}

for _ in range(l):
    now = input().rstrip()
    
    if now in waiting_dict:
        del waiting_dict[now]
        
    waiting_dict[now] = True 

result = list(waiting_dict.keys())

for i in range(min(k, len(result))):
    print(result[i])