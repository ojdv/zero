from sys import stdin
for s in stdin:
    n=int(s)
    if n == 0:
        break
    b=bin(n)
    c=len(b)
    d=len(b.strip('1'))
    print(c-d)