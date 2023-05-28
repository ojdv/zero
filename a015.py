import numpy as np
r,c=map(int,input().split())
x=[]
for i in range(r):
    x.append([int(x) for x in input().split()])
for i in range(c):
    for mat in x:
        print(mat[i], end=' ')
    print()