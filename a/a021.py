#大數運算
while True:
  try:
    s = input().replace('/','//')   # 轉換成除法求整數
    output = int(eval(f'{s}'))      # 使用 eval() 直接計算結果
    print(output)
  except:
    break