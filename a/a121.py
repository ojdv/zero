n,m=map(int,input().split())
count=0
for i in range(n,m+1):
    x=True
    for a in range(2,i):
        if i %a==0:
            x=False
            break
    if x:
        count+=1
print(count)