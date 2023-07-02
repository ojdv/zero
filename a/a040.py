while True:
  try:
    p, q = map(int, input().split(' '))  # 將輸入的文字轉換成兩個數字
    result = False                       # 預設 result 為 False
    for i in range(p, q):     # 取出 p q 範圍內的所有數字
      a = str(i)              # 數字轉換成文字
      m = len(a)              # 取得文字的長度
      b = 0                   # 預設變數 b 為 0
      for j in a:
        b = b + int(j)**m     # 設定 b 為每個數字乘以位數的加總
      if b == i:              # 如果符合阿姆斯壯數規則
        result = True         # 設定 result 為 True
        print(b, end=' ')     # 印出阿姆斯壯數
    if not result:
      print('none')           # 否則印出 none
  except:
    break