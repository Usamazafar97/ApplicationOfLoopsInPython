list=['1221','xyx','1234']
i=0
count=0
while i<len(list):
    print list[i]

    if list[i][0]==list[i][-1]:
        count+=1
        

    i+=1
print count