def to_check(split):
    if(split==list_to_check):
        return True
    else:
        return False

list_to_check="bobob"
list_to_check_in="azcbobobobobegghbobakl"
found=0

j=0
while j<len(list_to_check_in):
    i=0
    if(list_to_check[i]==list_to_check_in[j]):
        k=0
        index = j
        splitStr=""
        while k<len(list_to_check):
            if(index < len(list_to_check_in)):
                splitStr+=list_to_check_in[index]
            index+=1
            k+=1
        if(to_check(splitStr)==True):
            found+=1
    
    j+=1


print list_to_check+" found {}".format(found)+" times"