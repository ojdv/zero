
n = int(input())
px,py = map(int,input().split()) #first point
prev_d = 0 #first dir=East
left,right,back = 0,0,0 # count the turns
for i in range(n-1):
    x,y = map(int,input().split()) #current point
    #determine current dir
    if x > px: d = 0
    elif y < py: d = 1
    elif x < px: d = 2
    else: d = 3
    # determine turn
    turn = (d-prev_d)%4
    if turn==3: left += 1
    elif turn==1: right += 1
    elif turn==2: back += 1
    # current point become previous point of the next
    px,py = x,y
    prev_d = d
#end for
print(left,right,back)