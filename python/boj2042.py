import sys
# input = sys.stdin.readline
def _change(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff

    if start != end :
        _change(node*2, start, (start+end)//2, index, diff)
        _change(node*2+1, (start+end)//2+1, end, index, diff)

def _init(node, start, end):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    else :
        tree[node] = _init(node*2,start,(start+end)//2) + _init(node*2+1,(start+end)//2+1,end)
        return tree[node]

def _sum(node, start, end, left, right):
    if right < start or left > end :
        return 0
    if left <= start and end <= right:
        return tree[node]

    return _sum(node*2, start, (start+end)//2, left, right) + _sum(node*2+1, (start+end)//2+1, end, left, right)
# main
n, m, k = map(int,input().split())
num = []
tree = [0] * 3000000
for _ in range(n):
    num.append(int(input()))

_init(1,0,n-1)

# print(tree)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        diff = c - num[b-1]
        # print(diff)
        num[b-1] = c
        _change(1,0,n-1,b-1,diff)
    elif a == 2:
        print(_sum(1,0,n-1,b-1,c-1))
