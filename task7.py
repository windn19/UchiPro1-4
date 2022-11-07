x, y = ('abcdefgh87654321'.index(i) % 8 for i in input())
print(x, y)
derections = lambda i, j: (j - i == x - y) + (j + i == x + y) + ((j == x) != (i == y))
[print(*['.*Q'[derections(i, j)] for j in range(8)]) for i in range(8)]
