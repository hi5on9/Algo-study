import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
MAX_SIZE = 1234567890

def solution(board, moves):
    dolls = [[] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board)):
            dolls[i].insert(j,board[j][i])

    bucket = deque()
    for m in moves:
        m = m-1
        if m <0:break
        for idx,d in enumerate(dolls[m]):
            if d == 0: continue
            elif d!=0:
                dolls[m][idx] = 0
                bucket.append(d)
                break
    # print(dolls)
    pre = 0
    get_doll = len(bucket)
    temp = deque()
    while bucket:
        next = bucket.popleft()
        print("bucket",bucket)
        print("temp",temp)
        print()
        if temp:
            pre = temp.pop()
            if pre == next:
                pass
            else:
                temp.append(pre)
                temp.append(next)
        else:
            temp.append(next)
    print(temp)
    now_doll = len(temp)
    print(get_doll-now_doll)

    return get_doll-now_doll





board= [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)
