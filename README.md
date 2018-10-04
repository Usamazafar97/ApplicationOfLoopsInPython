# ApplicationOfLoopsInPython
1. Write a program that filters positive elements out of a list. The program should 
    build a new filtered list while the original list should remain unchanged. 
    For example, if a list containing the elements 2, -16, 2, -5, 0, 1, -2, -3 is used
    in the program, the program should build a new list containing -16, -5, -2, -3.
    Note the original ordering of the non-negative values is unchanged in the result.
    
2. Write a program that finds the smallest and largest substring in a given string.
    For example, if string contains following value = 'My Village is a beautiful place',
    your program should print "a" and “beautiful”.
    
3. Write a program that counts up the number of consonants contained in a string.
    Valid consonants are all the values except vowels: 'a', 'e', 'i', 'o', and 'u'. 
    For example, if string contains following value = 'azcbobobegghakl', your program 
    should print:

    Number of consonants: 10
    You can use raw_input function to take input from the user.
    
4. Write a program that prints the number of times the string 'bob' occurs in a user 
    input. For example, if string contains following value = 'azcbobobegghakl', then
    your program should print

    Number of times bob occurs is: 2
    You can use raw_input function to take input from the user.
    
5. Write a code that prints the most frequently occurring element of a list of integers.
    Break ties by choosing the lower value. For example, if the list passed contains the
    values [27, 15, 15, 11, 27], your method should return 15.
    
6. Islamabad Traffic office has asked you to create an application that grades the 
    written portion of the driver’s license exam. The exam has 20 multiple-choice 
    questions. Here are the correct answers:
   
    1. A	 6. B	11. A	16. C
    2. C         7. C	12. D	17. B
    3. A	 8. A	13. C	18. B
    4. A         9. C   14. A   19. D
    5. D	10. B	15. D	20. A
    
    Your program should store these correct answers in a list. The program should read
    the student’s answers for each of the 20 questions and store the answers in another
    list. After the student’s answers have been read, the program should display a 
    message indicating whether the student passed or failed the exam. (A student must 
    correctly answer 15 of the 20 questions to pass the exam.) It should then display 
    the total number of correctly answered questions, the total number of incorrectly 
    answered questions, and a list showing the question numbers of the incorrectly 
    answered questions.   
    
7. Write a Python program to count the number of strings where the string length is 2 
    or more and the first and last character are same from a given list of strings.

    Sample List: ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
    
8. Write a Python program to get a list, sorted in increasing order by the last element
    from a given list. Sample List: [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]] Expected 

    Result : [[2, 1], [1, 2], [2, 3], [4, 4], [2, 5]]
   
9. Write a Python program to create a list by concatenating a given list which range 
    goes from 1 to n.

    Sample list: ['p', 'q'] n =5 
    Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
   
10.Write a python program to calculate trace of matrix. Trace of an n-by-square 
    matrix is defined to be the sum of the elements on the main diagonal (the diagonal 
    from the upper left to the lower right).

    Mat= [[3, 4, 5], [1, 2, 3], [4, 7, 1]]
    Trace = 6
	
11.Write a Python function to check whether a number is perfect or not. According to
    Wikipedia : In number theory, a perfect number is a positive integer that is equal 
    to the sum of its proper positive divisors, that is, the sum of its positive divisors
    excluding the number itself (also known as its aliquot sum). Equivalently, a perfect
    number is a number that is half the sum of all of its positive divisors (including itself).
    Example: The first perfect number is 6, because 1, 2, and 3 are its proper positive
	divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum 
	of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number 
	is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
	
13.Write a function toNumbers(strList) that receives a list of strings as input, and
    converts each element from string to integer and updates the list so that it now contains
    integers. Each element of strList represents a number.	

14.The ancient Greeks classify numbers geometrically. For example, a number was called “triangular”
    if that number of pebbles could be arranged in a symmetric triangle. The first ten triangular 
    numbers are 0, 1, 3, 6, 10, 15, 21, 28, 36, and 45. Write and test the boolean function:	
    int isTriangular(int n)
    This function returns 1 if the given integer n is a triangular number, and 0 
    otherwise.
					.
				.	..
			.	..	...
		.	..	...	....
	.	..	...	....    .....	
	T1=1	T2=3	T3=6	T4=10   T5=15

15. Write a program that produces Christmas trees as output. It should have a function with two 
    parameters: one for the number of segments in the tree and one for the height of each segment.
    For example, the following tree on the left has 3 segments of height 4 and the one on the right 
    has 2 segments of height 5.	

	      *                              *
             ***                            ***
            *****                          *****
           *******                        *******
             ***                         *********
            *****                           ***
           *******                         *****
          *********                       *******
            *****                        *********
           *******                      ***********
          *********                          *
         ***********                         *
              *                           *******
              *
           *******           

17. Write a function named reverse_vertical that accepts a string as its parameter and prints each 
    letter of the string in reverse order in separate lines. For example, a call of reverse_vertical
    ("hey now") should produce the following output:

    w
    o
    n
    y
    e
    h

18. In physics, an object that is in motion is said to have kinetic energy. The following formula
    can be used to determine a moving object’s kinetic energy:

    KE =1/2 mv2

    The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass in 
    kilograms, and v is the object’s velocity in meters per second.
    Write a function named kinetic_energy that accepts an object’s mass (in grams) and velocity 
    (in kilometers per second) as arguments. The function should return the amount of kinetic energy 
    that the object has. Write a program that asks the user to enter values for mass and velocity, and
    then calls the kinetic_energy function to get the object’s kinetic energy.

19. Write a function that produces the following output. Use a function parameter to make it possible 
    to change the number of stairs in the figure. You can use write other helper functions as well.

                                          
                            o   ********         
                           /|\  *      *
                           / \  *      *
                      o   *******      *
                     /|\  *            *
                     / \  *            *
                o   *******            *
               /|\  *                  *
               / \  *                  *
          o   *******                  *
         /|\  *                        *
         / \  *                        *
     o  *******                        * 
    /|\ *                              *
    / \ *                              *
   *************************************

20. Write a function that produces the following rocket ship figure as its output. Use a function 
    parameter to make it possible to change the size of the rocket (the following output uses a size of
    2). You can use write other helper functions as well.

                                   /**\           
                                  //**\\          
                                 ///**\\\                          
                                ////**\\\\                      
                               /////**\\\\\     
                              +=*=*=*=*=*=*+                  
                              |../\..../\..|                             
                              |./\/\../\/\.|                             
                              |/\/\/\/\/\/\|                                      
                              |\/\/\/\/\/\/|                                     
                              |.\/\/..\/\/.|                                         
                              |..\/....\/..|                                        
                              +=*=*=*=*=*=*+                                     
                              |\/\/\/\/\/\/|                                     
                              |.\/\/..\/\/.|                                         
                              |..\/....\/..|                                         
                              |../\..../\..|                             
                              |./\/\../\/\.|                             
                              |/\/\/\/\/\/\|                                          
                              +=*=*=*=*=*=*+
                                   /**\           
                                  //**\\          
                                 ///**\\\                          
                                ////**\\\\                      
                               /////**\\\\\
                                                        
                                                 
                                                            
                                                         
                                                                  
                                                              

























	