#待解
import cmath

a, b, c = map(int, input().split())

# 计算判别式
d = b**2 - 4*a*c

# 计算根
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# 输出结果
if d < 0:
    print("No real root")
elif d == 0:
    print(f"Two same roots x={root1.real:.2f}")
else:
    print(f"Two different roots x1={root1.real:.2f}, x2={root2.real:.2f}")