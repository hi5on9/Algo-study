import sys
import heapq
import math
import re
from collections import deque
input = sys.stdin.readline
INF = 20


new_id = input().strip()


new_id = new_id.lower()
new_id = list(new_id)
# print("1step:",*new_id)
temp = ''

for i in range(len(new_id)):
    w = new_id[i]
    if '0' <= w <= '9' or 'a' <= w <= 'z' or w =='-' or w == '_' or w =='.':
        # print(w,end="")
        temp += w

# print("2step:",*temp)
while '..' in temp:
    temp = temp.replace('..', '.')

new_id = list(temp)

print("3step:",*new_id)

if len(new_id) > 0:
    if new_id[0] == '.':
        new_id.pop(0)

# print("4step:",*new_id)

if len(new_id) <= 0 :
    new_id.append('a')

# print("5step:",*new_id)


while(True):
    if len(new_id) <= 15:
        break
    else:
       new_id.pop()


# print("6step:",*new_id)

if len(new_id) > 0 :
    if new_id[len(new_id)-1] == '.':
        new_id.pop()

# print("7step:",*new_id)

if len(new_id) <= 2 :
    while(True):
        if len(new_id) == 3:
            break
        new_id.append(new_id[len(new_id)-1])

# print("8step:",*new_id)
answer = ''.join(new_id)
print(answer)
print(*new_id)
