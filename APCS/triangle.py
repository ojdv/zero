a, b, c = map(int, input().split())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a+b <= c:
    print(a, b, c)
if a+b <= c:
    print('No')
elif a*a+b*b == c*c:
    print(a, b, c, '\nRight')
elif a*a+b*b < c*c:
    print(a, b, c, '\nObtuse')
else:
    print(a, b, c, '\nAcute')

