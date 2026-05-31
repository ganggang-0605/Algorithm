from collections import deque


def solution(m, n, puddles):      
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    puddle = set([(p[1] - 1, p[0] - 1) for p in puddles])

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            
            if (i, j) in puddle:
                dp[i][j] = 0
            else:
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = (up + left) % 1000000007

    return dp[n-1][m-1]