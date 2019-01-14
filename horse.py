## Horse Race 
## By Joe Donahoe
## Inspired by Reid Hughes, who taught my high school computer science class in Turbo Pascal.  

import sys 

horseNames = []
horseSpeeds = []
horsePositions = []

def add_horse ( name, speed, position ):
    horseNames.append(name)
    horseSpeeds.append(speed)
    horsePositions.append(0)  ## not allowing advanced starting positions yet.  

def draw_board ( width ): 
    
    ## draw top border.  
    for i in range(width): 
        print("#", end="")    ## the end parameter prevents a newline.  
    print("")   ## just for the newline
    
    ## loop through horses. 
    for j in range(horseNames.count): 
        print("# ", end="") ## draw left border.  
        print(horseNames[j], end="")
        for k in range(len())
    
## stil in progress.  

