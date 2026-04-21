import sys

input = sys.stdin.readline

n, b, c = map(int, input().split())
a = list(map(int, input().split())) + [0, 0] 

ans = 0

if b <= c:
    print(sum(a) * b)
    exit()

for i in range(n):
    if a[i+1] > a[i+2]:
        m = min(a[i], a[i+1] - a[i+2])
        a[i] -= m
        a[i+1] -= m
        ans += m * (b + c)
        
        m2 = min(a[i], min(a[i+1], a[i+2]))
        a[i] -= m2
        a[i+1] -= m2
        a[i+2] -= m2
        ans += m2 * (b + 2 * c)
    
    else:
        m = min(a[i], min(a[i+1], a[i+2]))
        a[i] -= m
        a[i+1] -= m
        a[i+2] -= m
        ans += m * (b + 2 * c)
        
        m2 = min(a[i], a[i+1])
        a[i] -= m2
        a[i+1] -= m2
        ans += m2 * (b + c)
        
    ans += a[i] * b

print(ans)