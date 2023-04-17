n = int(input())
seg = []
for i in range(n):
    s, t = map(int, input().split())
    seg.append((s, t))
seg.sort()
left = 0
right = 0
length = 0
for (s, t) in seg:
    if s <= right:
        right = max(right, t)
    else:
        length += right-left
        left, right = s, t
length += right-left
print(length)
