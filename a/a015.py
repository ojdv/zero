from sys import stdin

# 讀入矩陣的行數和列數
for read in stdin:
    r, c = map(int, read.rstrip().split())
    matrix = [[int(x) for x in input().split()] for _ in range(r)]
    transposed_matrix = [[row[i] for row in matrix] for i in range(c)]
    for row in transposed_matrix:
        print(' '.join(map(str, row)))