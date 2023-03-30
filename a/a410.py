while True:
    try:
        # 將輸入的六個數字分配給 a、b、c、d、e、f 變數
        a, b, c, d, e, f = map(int, input().split(' '))
        if (a*e-d*b) != 0:     # 如果分母不為 0
            x = str(round((c*e-f*b)/(a*e-d*b), 2))  # 根據公式算出 x
            y = str(round((a*f-d*c)/(a*e-d*b), 2))  # 根據公式算出 y
            if '.' in x:
                if len([i for i in x.split('.')][1]) == 1:
                    x = x + '0'    # 如果有小數點，但小數點後方只有一位數，補一個零
            else:
                x = x + '.00'    # 如果沒有小數點，補兩個零
            if '.' in y:
                if len([i for i in y.split('.')][1]) == 1:
                    y = y + '0'    # 如果有小數點，但小數點後方只有一位數，補一個零
            else:
                y = y + '.00'    # 如果沒有小數點，補兩個零

            print(f'x={x}')
            print(f'y={y}')
        else:                 # 如果分母為 0
            if (c*e-f*b) == 0 and (a*f-d*c) == 0:
                print('Too many')    # 如果分子為 0，則有無窮解 ( x 和 y 可以是任意數 )
            else:
                print('No answer')   # 分子不為零則無解
    except:
        break
