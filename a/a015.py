from sys import stdin
for read in stdin:
    r, c = map(int, read.rstrip().split())
    matrix = []
    for i in range(r):
        matrix.append([int(x) for x in input().split()])
    for i in range(c):
        for mat in matrix:
            print(mat[i], end=' ')
        print()
