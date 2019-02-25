
import math

nk = input().split()
n = list(nk[0])
k = int(nk[1])

for _ in range(k):
    min_num = math.inf
    ii = 0
    for i in range(len(n)):
        n_copy = n.copy()
        n_copy.pop(i)
        nn = int(''.join(n_copy))
        if nn < min_num:
            min_num = nn
            ii = i
    n.pop(ii)

print(min_num)
