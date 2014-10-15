############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).
# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
x = 1
while x == 1:
    print "What is your temperature?"
    fever = int(raw_input())
    print "Have you been sick within the last 24 hours?"
    sick = raw_input()
    print "Have you been to West Africa recently?"
    westafrica = raw_input()
    if fever > 105:
        print "You need to be treated."
    if fever < 105:
        x = 1
    if fever > 102 and sick == "yes":
        print "You need to be treated."
        x = x - 1
    if sick == "yes" and westafrica == "yes":
        print "You need to be treated."
    if fever > 100 and westafrica == "yes":
        print "You need to be treated." 
    print "Are you the last patient?"
    patient = raw_input()
if patient == "yes":
    x = x - 1
