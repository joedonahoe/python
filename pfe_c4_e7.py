# Python for Everybody.  Chapter 4.  Exercise 7.  

# Rewrite grade program using function computegrade that takes score as a parameter and returns grade as a string.  

def getscore(): 
    score = input('Enter score: ')
    try: 
        score = float( score) 
    except: 
        print('Please input a numeric score.')
        exit()

    if score < 0 or score > 1: 
        print('Please input a numeric score between 1.0 and 0.0.')
        exit()

    return score 

def computegrade( score ): 
    if score >= 0.9: 
        return 'A'
    elif score >= 0.8: 
        return 'B'
    elif score >= 0.7: 
        return 'C' 
    elif score >= 0.6: 
        return 'D' 
    else:
        return 'F' 

score = getscore()
grade = computegrade( score )
print('For score ' + str(score) + ', the grade is ' + grade + '.')

