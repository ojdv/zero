n = int(input())
tmp = []
for i in range(2, int(1e9)):
    if n == 1:
        break
    x = 0
    while not n % i:
        x += 1
        n //= i
    if x:
        tmp.append([i, x])
ans = []
for i , x in tmp:
    if x > 1:
        ans.append(f'{i}^{x}')
    else:
        ans.append(i)
print(*ans, sep=' * ')