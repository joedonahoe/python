# Python for Everybody.  Chapter 3.  Exercises 1 and 2.  

# E1.  Rewrite the pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.  
# E2.  Use try and except to handle non-numeric input.  

try:
    hours = input( 'Enter Hours: ')
    hours = float( hours )
    rate = input( 'Enter Rate: ' ) 
    rate = float( rate )
except: 
    print('Please use numeric inputs.') 

if hours > 40: 
    pay = rate * 40 + rate * (hours - 40) * 1.5 
else:
    pay = rate * hours 

print( 'Pay: ' + str( pay ) ) 

