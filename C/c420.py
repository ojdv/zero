n = int(input())
for i in range(1, n+1):
    for j in range(n-i, 0, -1):  #前面的_
        print("_", end="")
    for j in range(1, i*2):
        print("*", end="")
    for j in range(n-i, 0, -1):  #後面的_
        print("_", end="")
    print()