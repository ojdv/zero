a = int(input())
x=[]#上傳時間
y=[]#上傳分數

for i in range(a):
    b , c=map(int,input().split()) #存取所有輸入
    x.append(b)
    y.append(c)

#最高分的時間點
q = -1
u = 0
for i in range(len(y)):
    if y[i]>q:
        q = y[i]#提交記錄中的最高分
        u = x[i]#最高分時間點

#紀錄嚴重錯誤的次數

j=0

for i in y:
    if i ==-1:
        j+=1

A = q-a-j*2

if A < 0:
    print(0,u)
else:
    print(A,u)