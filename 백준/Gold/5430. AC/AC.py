import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    temp = input().rstrip() 

    if n > 0:
        lst = deque(map(int, temp[1:-1].split(',')))
    else:
        lst = deque()
    
    error = False
    rev = False
    for i in p:
        if i == 'R':
            rev = not rev
        else:
            if not lst:
                error = True
                break
            if rev:
                lst.pop()
            else:
                lst.popleft()

    if error:
        print("error")
    else:
        if rev:
            lst.reverse()
        ans = "[" + ",".join(map(str, lst)) + "]"
        print(ans)