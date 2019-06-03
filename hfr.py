words = input().split()

out = []

for word in words:
    out.append(word[::-1])

print(*out)
