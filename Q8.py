list=[[2,5],[1,2],[4,4],[2,3],[2,1]]
i=0
count=0
while i<(len(list)-1):

    j=0
    while j<len(list[i]):

        if list[i][-1]<list[i+1][-1]:

            temp=list[i+1][-1]
            list[i+1][-1]=list[i][-1]
            list[i][-1]=temp
        j+=1

    i+=1
print list