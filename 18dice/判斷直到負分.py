while True:
    n=int(input())
    if n == -1:
        break
    if n >=60:
        print(n,'分及格',sep='')
    else:
        print(n,'分不及格',sep='')