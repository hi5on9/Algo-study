import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
from itertools import permutations
import math
word = input().replace("-"," ")
word = word.split()

answer = []

for w in word:
    if "'" in w:
        hype = w.split("'")
        afterHype = list(hype[1])[0]
        vowel = ["a","e","i","o","u","h"]
        preWord = ["c","j","n","m","t","s","l","d","qu"]
        if afterHype in vowel:
            if hype[0] in preWord:
                answer.append(hype[0])
                answer.append(hype[1])
            else:
                answer.append(w)
        else:
            answer.append(w)
    else:
        answer.append(w)

# print(answer)
print(len(answer))
