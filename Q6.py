list=["A","C","A","A","D","B","C","A","C","B","A","D","C","A","D","C","B","B","D","A"]

new_list=[]
i=0
while i<len(list):
    z=raw_input("enter the options in capital letter")
    new_list.append(z)
    i+=1
print new_list
j=0
incorrect_list=[]
correct=0
incorrect=0
while j<len(list):
    if(list[j]==new_list[j]):
        correct+=1

    else:
        incorrect+=1
        incorrect_list.append(list[j])
    j+=1

print "incorrect =",incorrect
print "correct =",correct
print "incorrect_list =",incorrect_list
if(correct>=15):
    print"As your correct answers are",correct,"so you passed the exam"
else:
    print"As your incorrect answers are",incorrect,"so you failed the exam"


        
