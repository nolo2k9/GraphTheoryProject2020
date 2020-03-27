#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Keith Nolan

#import the needed scripts and packages
import regex
import string
import random

#Ask user if they want to use a pre-defined expression or enter their own
print("A. Do you want to enter your own expression? (Press A) ")
print("B. Do you want to use a prefixed expression? (Press B)")
#setting up input variable
choice = input()
#the the user choose A then this will happen
if choice =='A' or choice =='a':
 #while true
 while True:
   
    print("Do you want to enter an expression? ")
    #if yes chosen the user can enter an expression
    keepGoing = input("Press Y for Yes or N for No \n")
    if keepGoing == 'y' or keepGoing == 'Y':
        True
    #if no chosen the loop will break
    elif keepGoing == 'N' or keepGoing == 'n':
        break
    #if satisfactory key not entered the user will be "stuck" until they make a valid selection
    else: 
         stuck = True
         while stuck:
             print("\n")
             print("==============================================")
             print("\n")
             print("Wrong selection entered!!! \n") 
             print("Do you want to enter another expression? \n")
             print("==============================================")
             keepGoing = input("Press y for yes or n for no \n")
              #if yes chosen the user will exit stuck loop and can enter a new expression
             if keepGoing == 'y' or keepGoing == 'Y':
                stuck = False
             #if no chosen the loop will break 
             elif keepGoing == 'N' or keepGoing == 'n':
                stuck = False
                
             else: 
                 stuck = True
     #if no chosen the loop will break           
    if keepGoing == 'n' or keepGoing == 'N':
        break
    #variable to get value for expression
    expression = input ("Enter expression : \n") 
    print("Expression entered: " + expression + "\n") 
    #variable to get value for string
    stringinput= input("Enter string : \n" ) 
    print("String entered  : " + stringinput + "\n") 
    #print result
    print (regex.match(expression, stringinput))




    '''
    if b is chosen a random expression will be generated from the lists of expressions and strings
    '''
elif choice =='B' or choice =='b':

 while True:
    #list of premade expressions
    exprList = ["a.b*","a.b","b","a", "a*", "b*", "b**", "a.b.b.c*", "a.c","c" ]
    #list of premade strings
    strList = ["bbbbbbbbbbbbbbb", "ab","a","b", "aaaaaaaaaaaaaaaaaaaa", "abc", "ac", "c"]
    #assigning a variable to a random string in the list using random.choice()
    expression = random.choice(exprList)
    #assigning a variable to a random string in the list using random.choice()
    string1 = random.choice(strList)
    print("\n")
    print("========================================================")
    #Output contents of expression variable
    print("The random expression chosen was: " + expression + "\n")
    #Output contents of string1 variable
    print("The random string choesen was: " + string1 + "\n")
    #Output results 
    print("output: ")
    print (regex.match(expression, string1))
    print("========================================================")
    print("\n")
    print("\n")
    #asking if the user wants another randomly generated expression 
    print("Do you want to get another random expression?")
    choice2 = input("Press Y for Yes or N for No")
    #input validation
    if choice2 == 'y' or choice2 == 'Y':
        continue

    elif  choice2 == 'n' or choice2 == 'N':
         break

    else: 
         stuck = True
         count = 1
         while stuck:
             print("\n")
             print("==============================================")
             print("\n")
             print("Wrong selection entered!!! \n") 
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




#Resources used
"""
code for taking input found on found on: 
https://www.geeksforgeeks.org/taking-input-in-python/
various python help
https://www.w3schools.com/python/python_operators.as
how to randomise variables
https://stackoverflow.com/questions/32288236/how-do-i-randomly-select-a-variable-from-a-list-and-then-modify-it-in-python
"""