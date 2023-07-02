a,b,c=map(int,input().split())
c1=max(a,b,c)
c2=min(a,b,c)
c3 = a+b+c-c1-c2
if c2+c3 <= c1:
    x='No'
elif c2**2+c3**2<c1**2:
    x='Obtuse'
elif c2**2+c3**2 == c1**2:
    x='Right'
elif c2**2+c3**2>c1**2:
    x='Acute'

print(c2,c3,c1)
print(x)