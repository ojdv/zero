n=int(input())
x=list(map(int,input().split()))
z=0
for i in x:
    z=max(z,i)
print(z)