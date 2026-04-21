import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MOD = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n + 1): 
        result = (result * i) % MOD
    return result

top = factorial(n)
bottom = (factorial(k) * factorial(n - k)) % MOD

inversed = pow(bottom, MOD - 2, MOD)

print((top * inversed) % MOD)

