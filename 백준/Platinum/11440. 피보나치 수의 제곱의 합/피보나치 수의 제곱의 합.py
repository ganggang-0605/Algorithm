import sys
MOD = 1000000007

def multiply(mat1, mat2):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= MOD
    return res

def power(mat, p):
    if p == 1: return mat
    half = power(mat, p // 2)
    half_sq = multiply(half, half)
    if p % 2 == 0: return half_sq
    else: return multiply(half_sq, mat)

n = int(sys.stdin.readline())
base_matrix = [[1, 1], [1, 0]]
ans_matrix = power(base_matrix, n)

print((ans_matrix[0][0] * ans_matrix[0][1]) % MOD)