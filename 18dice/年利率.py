while True:
    n = eval(input())
    x = eval(input())
    y = eval(input())
    if n == -1:
        break
    print("{:.2f}".format(n * x * y / 365))