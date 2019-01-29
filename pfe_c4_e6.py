# Python for Everybody.  Chapter 4.  Exercise 6.  

# Rewrite pay program using function computepay which takes two parameters, hours and rate.  

def computepay ( hours, rate ): 
    if hours > 40: 
        return rate * 40 + rate * (hours - 40) * 1.5 
    else:
        return rate * hours 
    
try:
    hours = input( 'Enter Hours: ')
    hours = float( hours )
    rate = input( 'Enter Rate: ' ) 
    rate = float( rate )
except: 
    print('Please use numeric inputs.') 

print( 'Pay: ' + str( computepay( hours, rate ) ) ) 