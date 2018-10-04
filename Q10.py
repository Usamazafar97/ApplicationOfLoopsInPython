list= [[3,4,5],[1,2,3],[4,7,1]]
print "list =",list
i=0
sum=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if (i==j):
            sum+=list[i][j]
        j+=1
    i+=1
print "Trace =",sum