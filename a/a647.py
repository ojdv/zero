n = int(input())
for i in range(n):
  m, p = map(int, input().split())   # 將 m 和 p 轉換成數字
  r = (p-m)/m*100          # 因為輸出結果為百分比，所以乘以 100
  if r<0:
    r = r - 0.000001       # 如果結果小於 0，減去處理誤差的數值
  elif r>0:
    r = r + 0.000001       # 如果結果大於 0，加上處理誤差的數值
  if r >= 10 or r <= -7:   # 進行獲利的邏輯判斷
    t = 'dispose'
  else:
    t = 'keep'
  print(f'{r:.2f}% {t}')   # 使用字串格式化的方式輸出，取出小數點兩位數