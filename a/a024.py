def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)


a, b = (input().split())
print(GCD(int(a), int(b)))
