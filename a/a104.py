while True:
    try:
        n=int(input())
        x=list(map(int,input().split()))
        a=sorted(x)
        print(*a)
    except:
        break
