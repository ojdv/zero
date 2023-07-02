count = int(input())
ans = []

for i in range(count):
    rule = ""
    l1 = input().split()
    l2 = input().split()

    # rule A
    if l1[1] == l1[3] or l1[1] != l1[5] or l2[1] == l2[3] or l2[1] != l2[5]:
        rule += "A"
    # rule B
    if l1[-1] == '0' or l2[-1] == '1':
        rule += "B"
    # rule C
    if l1[1] == l2[1] or l1[3] == l2[3] or l1[5] == l2[5]:
        rule += "C"

    if rule == "":
        ans.append(None)
    else:
        ans.append(rule)


for a in ans:
    print(a)