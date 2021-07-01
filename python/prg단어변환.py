import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
MAX_SIZE = 1234567890

def solution(begin, target, words):
    v = [0] * len(words)
    if not (target in words):
        print(0)
        return 0

    q = deque()
    q.append((begin,0))
    ans = MAX_SIZE
    while q:
        now,change = q.popleft()
        if now == target:
            if ans > change:
                ans = change
        n_list = list(now)
        print(now,change)
        print(q)
        print(words)
        for idx,w in enumerate(words):
            w_list = list(w)
            cnt = 0
            for j,i in enumerate(w_list):
                if i == n_list[j]:
                    cnt +=1
            if cnt == len(now) - 1 and v[idx] == 0:
                q.append((w,change+1))
                v[idx] = 1
                if w == target:
                    v[idx]= 0



    print(ans)
    return ans
begin = 'hit'
target = 'hhh'
words = ['hhh','hht']
word = ['hot','dot','dog','lot','log','cog']
word2 = ['hot','dot','dog','lot','log']
solution(begin,target,words)
