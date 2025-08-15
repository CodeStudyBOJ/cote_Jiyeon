import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()

count = 0
i = 0
j = N - 1

while i < j:
    s = A[i] + A[j]
    if s < M:
        i += 1
    elif s > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
