while True:
    n=eval(input())
    if n == -1:
        break
    x=eval(input())
    y=eval(input())
    a=n*x*y/365
    print("{:.2f}".format(a))