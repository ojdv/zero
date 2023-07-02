n=int(input())
count=0
c=0
b=0
for i in range(n):
    x=int(input())
    if x %3==0:
        count+=1
    elif x%3==1:
        c+=1
    else:
        b+=1
print(count,c,b)