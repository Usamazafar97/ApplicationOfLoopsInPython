n=input("enter the no.")
i=1
sum=0
while i<n:
    if(n%i==0):

        sum=i
        sum+=sum
    i+=1
if(sum==n):
    print "number is perfect"
else:
    print "number is not perfect"