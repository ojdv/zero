while True:
  try:
    n = int(input())
    f = 0
    g = 0
    for i in range(1,n+1):
      f +=i 
      g +=f
    print(f, g)
  except:
    break