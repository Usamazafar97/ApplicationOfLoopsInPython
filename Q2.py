#list="my village is a beautiful place"
#string=[]
#i=0
#k=" "
#z=""
#count=0
#max=-1000
#min=1000

#while i<len(list):
#    if(list[i]!=" "):
#        count+=1
#        z+=list[i]
#        string+=list[i]
#        if(count>max):
#            max=count
#            a=string
#        if(count<min):
#            min=count
#            b=string
#    else:
#        count=0
#        string=''
#        z=""
    
#    i+=1

#print a

list="my village is a beautiful place"
splitlist = list.split(" ")

i=0
max=0
maxWord= ""
min=len(list)
minWord= ""
while i<len(splitlist):

    if(max<len(splitlist[i])):
        maxWord = splitlist[i]
        max=len(splitlist[i])
    if(min>len(splitlist[i])):
        minWord = splitlist[i]
        min=len(splitlist[i])
    i+=1

print "maxWord=",maxWord
print "minWord=",minWord
