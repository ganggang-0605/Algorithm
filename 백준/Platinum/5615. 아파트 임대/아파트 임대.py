import sys
input = sys.stdin.readline

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def miller_rabin(n, a):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d // 2
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False

def is_prime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    alist = [2, 7, 61]
    for a in alist:
        if n == a: return True
        if not miller_rabin(n, a): return False
    return True

n = int(input())
cnt = 0
for _ in range(n):
    temp = int(input())
    if is_prime(2 * temp + 1):
        cnt += 1
print(cnt)