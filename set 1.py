n = int(input())
in_strs = []

for _ in range(n):
    in_strs.append(input())

in_zip = list(zip(*in_strs))

result = []
for t in in_zip:
    if all(tt == t[0] for tt in t):
        result.append(t[0])
    else:
        break

print(''.join(result))
