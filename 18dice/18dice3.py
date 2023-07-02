while True:
    x = eval(input())
    y = eval(input())
    if x == 0.0 and y == 0.0:
        break
    elif x > 0.0 and y > 0.0:
        print("第一象限")
    elif x < 0.0 and y > 0.0:
        print("第二象限")
    elif x < 0.0 and y < 0.0:
        print("第三象限")
    elif x > 0.0 and y < 0.0:
        print("第四象限")
    elif x == 0.0:
        print("y軸")
    else:
        print("x軸")
