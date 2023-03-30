T = int(input())
for i in range(T):
    ans = 1
    for x in input():
        ans *= int(x)
    print(ans)
