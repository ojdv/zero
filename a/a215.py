while True:
    try:
        n, m = map(int, input().split(' '))
        a = 0
        b = 0
        while True:
            a = a + 1
            b = b + n
            n = n + 1
            if b > m:
                break
        print(a)
    except:
        break
