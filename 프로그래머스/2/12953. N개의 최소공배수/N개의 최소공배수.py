import math
from functools import reduce

def get_lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    return reduce(get_lcm, arr)