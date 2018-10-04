def boolean(n):
    a=((8*n)+1)**.5
    b=(a-1)/2.0
    if(b%1==0):
        c=1
    else:
        c=0
    return c

n=input("enter the number to chk")
print boolean(n)