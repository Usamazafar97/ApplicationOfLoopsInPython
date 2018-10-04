height=input("enter the height")
q=0
i=-2
segment=3
while q<segment:
    stars=7
    star=(stars+1)/2
    spaces=(stars/2)+1
    i=0
    while i<stars:
        j=0
        while j<spaces:
            print " ",
            j+=1
        k=0
        while k<i+1:
            print "*",
            k+=1
        print
        spaces-=1
        i+=2

    i+=2
    q+=1