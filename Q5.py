list=[27,15,13,11,27,11,11]
i=0
max=-1000
count=1
while i<len(list):
    j=i+1
    while j<len(list):
        if(list[i]==list[j]):
            count+=1

        j+=1
        if(count>max):

            max=count
            z=list[i]
            count=0

    i+=1
print z