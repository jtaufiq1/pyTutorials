#!/usr/bin/python3

# Get number between 10 and 20 inclusive
# If number is within range
#   Output Thank you
# Else
#   Output Incorrect answer

num = int(input("Enter a number between 10 and 20: "))

if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
