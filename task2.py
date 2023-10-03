#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

answer = input("the number is ")
answer = int
if answer >= int(0):
    print("positive")

if answer == int(0):
    print("zero")

if answer <= int(0):
    print("negative")