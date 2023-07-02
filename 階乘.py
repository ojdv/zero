def function(n):
    if n == 0:
        return 1
    else:
        return n*function(n-1)
n=int(input())
print(function(n))