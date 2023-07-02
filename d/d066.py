a,b=map(int,input().split())
x=a*60+b
if 7*60+30 <= x<17*60+0:
    print('At School')
else:
    print('Off School')