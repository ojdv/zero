a = int(input())
z = []
p = []
A=0
B=[]
for i in range(a):
    b = list(map(int, input().split()))
    z.append(b)

for i in range(len(z)-1):
    p.append(abs(z[i][0] - z[i + 1][0]) + abs(z[i][1] - z[i + 1][1]))

p=sorted(p)

print(p[-1],p[0])