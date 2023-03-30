a, b, c = map(int, input().split())
m1 = max(a, b, c)
m2 = min(a, b, c)
m3 = a+b+c-m1-m2
if m2+m3 <= m1:
    print(m2, m3, m1, '\nNo')
elif m2**2+m3**2 < m1**2:
    print(m2, m3, m1, '\nObtuse')
elif m2**2+m3**2 == m1**2:
    print(m2, m3, m1, '\nRight')
elif m2**2+m3**2 > m1**2:
    print(m2, m3, m1, '\nAcute')
