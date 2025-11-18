"""
Full Name: Ritesh Rashid Osman
Class-Section: Fa25 IS 250-01 Application Program Development I
Assignment Title: Files and Exceptions Project
Submission Date: 11/17/25
"""
"""
1. Start by defining a function naming it calculate_average
2. Within the confines of the function, request the user to type the first exam score
3. Subsequently request the user to type the second exam score
4. Finally prompt the user to enter the third exam score
5. The three inputs should then all be converted into numbers
6. Calculate the average by adding the three scores and dividing it by three
7. The scores should then be printed on it's own line 
8. The grand average score should be printed on it's very own line
9. Terminate the function
10. Call the function at the bottom of the program 
"""


def calculate_average():
    # Request the user to enter the first score. This will be done two more times
    score1 = float(input("Enter first score: "))
    # Request the user to enter the second score
    score2 = float(input("Enter second score: "))
    # Request the user to enter the third score
    score3 = float(input("Enter third score: "))
    # Using the formula below we can calculate the average of the three scores
    average = (score1 + score2 + score3) / 3
    # Print the first score.
    print("First score:", score1)
    # Print the second score.
    print("Second score:", score2)
    # Print the third score
    print("Third score:", score3)\
    # Now finally print the average score
    print("The average score is:", average)
# Call your function when your program is ready
calculate_average()   
  
