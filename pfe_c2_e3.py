# Python for Informatics.  Chapter 2.  Exercise 3.  

# Write a program to prompt the user for hours and rate per hour to compute gross pay.  

hours = input( 'Enter Hours: ')
rate = input( 'Enter Rate' ) 
print( 'Pay: ' + str( float(hours) * float(rate) ) ) 
