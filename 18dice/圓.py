while True:
    n=eval(input())
    if n <=0:
        break
    a=n/3.14/2
    print('半徑',round(a,2),sep='')
    print('面積',round(a**2*3.14,2),sep='')