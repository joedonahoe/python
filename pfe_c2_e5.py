
###############################################################################
# Python for Informatics.  Chapter 2.  Exercise 5.  
###############################################################################
# Write a program which prompts the user for a Celsius temperature, convert the 
# temperature to Fahrenheit, and print out the converted temperature.  
###############################################################################

tempC = input('Enter a temperature in Celsius: ')
tempC = float( tempC )
tempF = tempC * 9/5 + 32 
print('The temperature in Fahrenheit is ' + str(tempF) )