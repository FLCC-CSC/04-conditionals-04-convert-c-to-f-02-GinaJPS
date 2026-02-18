# FILE NAME - convert_C_to_F_02.py

# NAME: Regina Swartout
# DATE: 2/18/26
# BRIEF DESCRIPTION:  A program that will first ask the user if they would like to convert from Celsius to Fahrenheit 
# or from Fahrenheit to Celsius. Once the conversion has been established the user is prompted to enter a temperature 
# and the equivalent temperature is output to the screen.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====")
print()
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")

print()
choice = int(input("Please choose from the above menu: "))
temp = float(input("Enter a temperature to convert: "))
print()

if choice == 1:
  fahrenheit = (temp * 9) / 5 + 32
  print(f'{temp} degrees Celsius is {fahrenheit} degrees Fahrenheit.')
else:
  celsius = (temp - 32 ) * 5/9
  print(f'{temp} degrees Fahrenheit is {celsius} degrees Celsius.')










########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
I learned that it is ok to use empty print lines to create spaces instead of using the new line escape character, 
and by using the empty print lines it helps you to better visualize what the output formatting will look like.

I also learned that the grading system is very sensitive.  I am submitting this again, hoping that the errors I 
got were because I didn't put two spaces in front of the menu items.







'''