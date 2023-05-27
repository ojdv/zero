from math import sqrt
a, b, c = map(int, input().split())
judge = b*b-(4*a*c)
if judge < 0:
    print("No real root")
    exit(0)
root1 = int((-b + sqrt(judge))/(2*a))
root2 = int((-b - sqrt(judge))/(2*a))
if root1 == root2:
    print(f"Two same roots x={root1}")
else:
    print(f"Two different roots x1={max(root1,root2)} , x2={min(root1,root2)}")
