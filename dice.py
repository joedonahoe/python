
## Rolling Dice Simluator
## By Joe Donahoe
## Idea from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
## 2019.01.13.  JSD.  Created program with basic 3d7.  

import random ## needed for random numbers  

def ConductExperiment ( number_of_rolls, number_of_dice, dice_sides ): 
    total_result = 0 
    for i in range( number_of_rolls ): 
        total_result = total_result + RollDice ( number_of_dice, dice_sides )
    return( total_result / number_of_rolls)

def RollDice ( number_of_dice, dice_sides ): 
    total_result = 0 
    for i in range( number_of_dice ): 
        total_result = total_result + random.randint(1,dice_sides)
    return( total_result )

r = 100
d = 3 
s = 6 
print('Rolled a ' + str(d) + 'v' + str(s) + ', ' + str(r) + ' times, and we averaged ' + str(ConductExperiment ( 100, 3, 6 )) + '.' ) 


        

