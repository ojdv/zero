x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if (b-a)==(c-b)==(d-c):
        print(a,b,c,d,d+(d-c))
    elif (b/a)==(c/b)==(d/c):
        print(a,b,c,d,d*(d//c))