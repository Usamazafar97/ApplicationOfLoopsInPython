ListSize = input("Enter List Size:")
List = []
element = ""
i=0
while(i<ListSize):
    element = raw_input("Enter Element No {}".format(i)+" :")
    List.append(element)
    i+=1

print List

n = input("Enter n:")
FinalList = []
NewElement = ""

j=0
while (j<n):
    i=0
    while(i<ListSize):
        NewElement = List[i] + "{}".format(j+1)
        FinalList.append(NewElement)
        i+=1
    j+=1

print FinalList