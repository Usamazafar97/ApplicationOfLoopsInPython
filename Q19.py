NumOfStairs = input("Enter Number of Stairs:")
stairWidth = 7

def printFigure(beforeManSpaces,afterManSpaces,StairNum,iVal):
    totalWidth = beforeManSpaces+afterManSpaces;
    #print totalWidth
    j=0
    while (j<6):
        k=0
        str1=""
        while(k<totalWidth):
            if(k<=beforeManSpaces-stairWidth-1):
                str1+=" "
            elif(k>(beforeManSpaces-stairWidth-1) and k<totalWidth-afterManSpaces):
                if(j == 0):
                    str1+="  (O)  *"
                elif(j == 2):

                    str1+="  /|\\  *"
                elif(j == 4):
                    str1+=" / | \\ *"
                elif(j == 1 or j == 3):
                    str1+="   |   *"
                else:
                    str1+="********"
                k+=7                
            else:
                if(j == 0):
                    if(StairNum==0):
                            str1+="*"
                    elif( k==totalWidth-1): 
                        str1+="*"
                    else:
                        str1+=" "                
                else:
                    if(j == 5 and  iVal == 1):
                        str1+="*"
                    else:
                        if( k==totalWidth-1): 
                            str1+="*"
                        else:
                            str1+=" "
            k+=1
        print str1
        j+=1    
    #print "Function Ended"



i=NumOfStairs
while i>=1:
    #print "loop =",i
    printFigure(stairWidth*i,stairWidth*(NumOfStairs-i)+stairWidth,NumOfStairs-i,i)
    i-= 1 


