
## Rolling Dice Simluator
## By Joe Donahoe
## Idea from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
## 2019.01.13.  JSD.  Created program with basic 3d7.  

import random ## needed for random numbers  

def ConductExperiment ( number_of_rolls, number_of_dice, dice_sides, adder ): 

    results = [] 

    ## roll dice
    minResult = number_of_dice * dice_sides + adder ## initialize to maximum possible value.  
    maxResult = 0  ## not expecting adder to be negative and less than number_of_dice * dice_sides
    totalResult = 0
    for i in range( number_of_rolls ): 
        result = 0
        for j in range( number_of_dice ): 
            result = result + random.randint(1,dice_sides) + adder
        if result < minResult: 
            minResult = result
        if result > maxResult: 
            maxResult = result
        totalResult = totalResult + result
        results.append ( result ) 
    averageResult = totalResult / number_of_rolls

    ## describe the experiment.  
    if adder == 0: 
        adderText = ""
    elif adder > 0: 
        adderText = "+"+str(adder) 
    else: 
        adderText = str(adder) ## expecting the minus sign to be reported
    print('We rolled a ' + str(number_of_dice) + 'd' + str(dice_sides) + adderText + ', ' + str(number_of_rolls) + " times.") 

    ## print stats about the experiement.  
    print("MIN = " + str( minResult ) )
    print("MAX = " + str( maxResult ) )
    print("AVG = " + str( averageResult ) )

    ## print a histogram.  
    currentResult = minResult 
    while currentResult <= maxResult: 
        if currentResult < 10: 
            print( " ", end='' )
        print( str(currentResult) + ' :: ', end='' )
        for i in results: 
            if i == currentResult: 
                print( "x", end="" )
        print( "" ) ## for newline
        currentResult = currentResult + 1 

ConductExperiment ( 500, 3, 6, 0 ) 



        

