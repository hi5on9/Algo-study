import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
from itertools import permutations
import math


# 국어 점수가 감소하는 순
# 같으면 영어 증가하는 순
# 영어 국어 같으면 수학 감소 순
# 모든 점수 같으면 이름이 사전 순으로 증
N = int(input())
student = []
for n in range(N):
    student.append(list(input().split()))

student.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for s in student:
    print(s[0])
