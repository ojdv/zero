while True:
    x=[]
    n=int(input())
    if n == 0:
        break
    for i in range(1,n):
        if i %7!=0:
            x.append(i)
    print(*x)