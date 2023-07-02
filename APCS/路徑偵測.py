r = [0,0]
z = [0,0,0]
now = "r"
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a != r[0]:
        if a > r[0]:
            if now == 'l':
                z[2] += 1
            elif now == 'u':
                z[0] += 1
            elif now == 'o':
                z[1] += 1
            now = 'r'
        if a < r[0] :
            if now == 'r':
                z[2] += 1
            elif now == 'o':
                z[0] += 1
            elif now == 'u':
                z[1] += 1
            now = 'l'
    elif b != r[1]:
        if b > r[1]:
            if now == 'u':
                z[2] += 1
            elif now == 'r':
                z[0] += 1
            elif now == 'l':
                z[1] += 1
            now = 'o'
        if b < r[1] :
            if now == 'o':
                z[2] += 1
            elif now == 'l':
                z[0] += 1
            elif now == 'r':
                z[1] += 1
            now = 'u'
    r = [a,b]
print(z[0],z[1],z[2])