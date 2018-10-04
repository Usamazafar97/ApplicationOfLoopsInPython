import math
PI = 22.0/7.0
T = 2*PI
def f(t):
    val=0
    if(t>0 and t<(T/2.0)):
        val=1
    if(t==(T/2.0)):
        val=0
    if(t>(T/2.0) and t<(T)):
        val=-1
    return val
def S(t,n):
    i=0
    val=0
    sum = 0
    while i<n:
        res1=(1.0/(2*i-1))
        res2=math.sin((2*((2*i)-1)*PI*t)/T)
        sum+= res1*res2
        i+=1
    val=(sum)*(4.0/PI)
    return val
def Calculate_t(alpha):
    return alpha*T
List_alpha = [0.01,0.25,0.49]
List_n = [1,3,5,10,30,100]
j=0
while(j<len(List_alpha)):
    i=0
    alpha = List_alpha[j]
    t = Calculate_t(alpha)
    print "For ALPHA = ",alpha," t = ",t
    print "n\t\tf(t)\t\tS(t,n)\t\t\tERROR"
    while(i<len(List_n)):
        n = List_n[i]
        error = f(t)-S(t,n)
        print n,"\t\t",f(t),"\t\t",S(t,n),"\t\t",error
        i+=1
    j+=1


