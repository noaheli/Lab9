############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer
print "Please insert a temperature (Celcius)"
userinput = int(raw_input())
userinput = userinput * 9
userinput = userinput / 5
userinput = userinput + 32
print "Here is the Fahrenheighttemperature."
print userinput