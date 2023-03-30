z = int(input())
for i in range(1, z+1):
    a = int(input())
    b = int(input())
    cnt = 0
    for k in range(1, 32+1):
        if k**2 < a:
            continue
        if k**2 > b:
            break
        cnt += k**2
    print(f'Case {i}: {cnt}')
