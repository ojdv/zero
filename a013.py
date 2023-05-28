w = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
 
def num(n):
    n = n[::-1]
    m = w[n[0]]
    for i in range(1,len(n)):
        if w[n[i]]<w[n[i-1]]:
            m-=w[n[i]]
        else:
            m+=w[n[i]]
    return(m)
 
p = [["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
 
def roma(n):
    r = ""
    for i in p:
        x = divmod(n,i[1])
        if x[0]!=0:
            r += i[0]*x[0]
            n = x[1]
    return r
 