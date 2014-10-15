############################################
#                                          # 
#                   85pt                   #
#             Who has a fever?             #
############################################

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

myList = [102,98,96,101,100,99,103,97,98,105]
fever = []
# Insert for loop here


# This should print [102,101,103,105]
for fever1 in myList:
    if fever1 > 100:
        fever.append(fever1)
print fever
