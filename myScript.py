# Author: Keith Nolan
#run the regex file 
#import the regex script
import regex
import random
import string


import random

"""
code for taking input found on found on: 
https://www.geeksforgeeks.org/taking-input-in-python/

https://www.w3schools.com/python/python_operators.as
"""



print("A. Do you want to enter your own expression? (Press A) ")
print("B. Do you want to use a prefixed expression? (Press B)")
choice = input()
if choice =='A' or choice =='a':
    
 while True:
   
    print("Do you want to enter an expression? ")
    keepGoing = input("Press Y for Yes or N for No \n")
    if keepGoing == 'y' or keepGoing == 'Y':
        True
    elif keepGoing == 'N' or keepGoing == 'n':
        break
    else: 
         stuck = True
         count = 1
         while stuck:
             print("\n")
             print("==============================================")
             print("\n")
             print("Wrong Expression entered!!! \n") 
             print("Do you want to enter another expression? \n")
             print("==============================================")
             keepGoing = input("Press y for yes or n for no \n")
             if keepGoing == 'y' or keepGoing == 'Y':
                stuck = False
             elif keepGoing == 'N' or keepGoing == 'n':
                stuck = False
                
             else: 
                 stuck = True
    if keepGoing == 'n' or keepGoing == 'N':
        break

    expression = input ("Enter expression : \n") 
    print("Expression entered: " + expression + "\n") 
    stringinput= input("Enter string : \n" ) 
    print("String entered  : " + stringinput + "\n") 

    print (regex.match(expression, stringinput))




    
elif choice =='B' or choice =='b':

 while True:

    exprList = ["a.b*","a.b","b","a", "a*"]
    strList = ["bbbbbbbbbbbbbbb", "ab","a","b","b*", "b**", "aaaaaaaaaaaaaaaaaaaa"]

    expression = random.choice(exprList)
    string1 = random.choice(strList)
    print("\n")
    print("========================================================")
    print("The random expression chosen was: " + expression + "\n")
    print("The random string choesen was: " + string1 + "\n")
    print("output: ")
    print (regex.match(expression, string1))
    print("========================================================")
    print("\n")
    print("\n")
    print("Do you want to get another random expression?")
    choice2 = input("Press Y for Yes or N for No")
    if choice2 == 'y' or choice2 == 'Y':
        continue

    elif  choice2 == 'n' or choice2 == 'N':
         break


   
