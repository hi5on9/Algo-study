import sys
input = sys.stdin.readline
from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def find(a,network):
    if a == network[a]:
        return a
    network[a] = find(network[a],network)
    return network[a]

def union(a,b,network):
    a = find(a,network)
    b = find(b,network)

    if a!=b :
        network[b] = a

def solution(n, computers):
    network = [i for i in range(n)]
    answer = set()

    for i in range(n):
        for j in range(n):
            if i==j:continue
            if computers[i][j] == 1:
                a = find(i,network)
                b = find(j,network)
                if a!= b:
                    union(a,b,network)
                print(network)

    for net in network:
        n = find(net,network)
        answer.add(n)
    print(answer)
    print(len(answer))
    return len(answer)



solution(n,computers)
