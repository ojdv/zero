while True:
    try:
        a = list(input())
        b = a[::-1]
        x = ''.join(b)
        print(int(x))
    except:
        break
