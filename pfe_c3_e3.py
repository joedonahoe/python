# Python for Everybody.  Chapter 3.  Exercise 3.  

# Write a program to prompt for a score betwee 0.0 and 1.0.  If the score 
# is out of range, print an error message.  If the score is between 0.0 
# and 1.0, print a grade.  

score = input('Enter score: ')
try: 
    score = float( score) 
except: 
    print('Please input a numeric score.')
    exit()

if score < 0 or score > 10: 
    print('Please input a numeric score between 10.0 and 0.0.')
    exit()
else: 
    if score >= 0.9: 
        grade = 'A'
    elif score >= 0.8: 
        grade = 'B'
    elif score >= 0.7: 
        grade = 'C' 
    elif score >= 0.6: 
        grade = 'D' 
    else:
        grade = 'F' 

print('For score ' + str(score) + ', the grade is ' + grade + '.')

