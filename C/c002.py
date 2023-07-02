def f91(N):
    if N <= 100:
        return f91(f91(N+11))
    else:
        return N-10

while True:
    N = int(input())
    if N == 0:
        break
    print('f91(' + str(N) + ') = ',str(f91(N)),sep='')