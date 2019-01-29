# Python for Everybody.  Chapter 5.  Exercise 1.  

# Write a program which repeatedly reads numbers until the user 
# enters "done".  Then print the total, count, and average.  

def isNumber( n ): 
    try:
        n = float(n)
        return True
    except: 
        return False 

count = 0
total = 0
minVal = False 
maxVal = False

while True:
    inputValue = input('Enter a number: ') 
    if inputValue == 'done': 
        break
    elif not isNumber( inputValue ): 
        print('Invalid Input')
    else:  
        inputValue = float(inputValue)
        count = count + 1
        total = total + inputValue
        if minVal == False: 
            minVal = inputValue 
        else: 
            if minVal > inputValue: 
                minVal = inputValue 
        if maxVal == False: 
            maxVal = inputValue 
        else:
            if maxVal < inputValue: 
                maxVal = inputValue 

if count == 0: 
    print('No data was given.')
else:            
    print('Summary :: count='+str(count)+' sum='+str(total)+' avg='+str(total/count)+' min='+str(minVal)+' max='+str(maxVal))
