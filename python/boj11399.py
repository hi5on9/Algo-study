import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
from itertools import permutations
import math

N = int(input())
num = list(map(int, input().split()))
num = sorted(num, reverse=True)

answer = 0
for idx,n in enumerate(num):
    answer += (idx+1) * n

print(answer)
