while True:
    try:
        a, b, c = map(int, input().split(' '))   # 將題目給予的字串拆分成 a、b、c 三個數字
        rd = a*(10**c)//b    # 乘以 10^位數 後除以 b 求整數
        rs = str(rd)         # 將整數轉成字串
        if len(rs) < c:      # 如果字串的長度不足位數
            for i in range(c - len(rs)):
                rs = '0' + rs    # 將字串前方補 0
        m = rs[(c*-1):]      # 根據位數拆分字串 ( 小數點後段 )
        n = rs[:(c*-1)]      # 根據位數拆分字串 ( 小數點前段 )
        if n == '': n = '0'  # 如果前段為空字串，就補 0
        print(f'{n}.{m}')    # 加上小數點，印出結果
    except:
        break