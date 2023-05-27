x = [int(l) for l in input()]
diff = 0
for i in range(len(x)):
    if i % 2:
        diff += x[i]
    else:
        diff -= x[i]
print(abs(diff))
