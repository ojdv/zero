while True:
    try:
        x=int(input())
        if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0):
            print('閏年')
        else:
            print('平年')
    except:
        break