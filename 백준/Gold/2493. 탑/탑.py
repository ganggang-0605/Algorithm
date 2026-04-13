import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = []

for i in range(n):
    height = lst[i]

    while stack:
        if stack[-1][1] < height:
            stack.pop()
        else:
            ans.append(stack[-1][0] + 1)
            break

    if not stack:
        ans.append(0)

    stack.append((i, height))

print(*ans)