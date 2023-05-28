num=int(input())
result={}
while True:
        for i in range(2,num+1):
            if num%i== 0:
                if i in result:
                    result[i]= result[i]+1
                else:
                    result[i] = 1
                num = num//i
                break
            if num == 1:
                break
        print(result)
