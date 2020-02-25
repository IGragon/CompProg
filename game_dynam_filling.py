f = open("input.txt", mode="r")

f = f.readlines()

n = int(f.pop(0))

matches = [0 for i in range(n + 1)]

k = int(f.pop(0))
moves = list(map(int, f.pop(0).split()))
'''for _ in range(k):
    moves.append(int(f.pop(0)))'''

for i in range(min(moves)):
    matches[i] = 2

for i in range(min(moves), n + 1):
    for move in moves:
        if i - move >= 0:
            if matches[i - move] == 2:
                matches[i] = 1
                break
    if matches[i] == 0:
        matches[i] = 2

print(matches)
print(matches[-1])
