list=[2,-16,2,-5,0,1,-2,-3]
new_list=[]
i=0

while i<len(list):

    if (list[i]<0):
        new_list.append(list[i])

    i+=1
print new_list

