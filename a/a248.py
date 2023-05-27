from pwn import *
r = remote("120.114.62.214", 2406)
r.recvlines(14)

for i in range(100):
    r.recvline()

    idd = r.recvline().split()

    ap = idd[2].decode()
    print(ap)
    summ = 0
    ill = 0
    print(len(idd[2]))

    for f in range(1, 10):
        summ += int(ap[f])
    if (len(idd[2]) == 10) and (summ % 3 == 0) and ('A' <= ap[0] <= 'Z'):
        ill = 1
    else:
        ill = 0

    r.recvuntil("answer : ")
    if ill == 1:
        r.sendline("valid")
        print(b"valid")
    else:
        r.sendline("invalid")
        print(b"invalid")
print(r.recvline().decode())


r.close()
