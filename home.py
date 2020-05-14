#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Keith Nolan

#import the needed scripts and packages
import regex
import string
import random

def ownExpr():
    print("**********************************************************")
    print("(A).")
    print("-To enter in your own regular expression and string")
    print("Please enter the following into the cmd prompt: ")
    print("python ownExpr.py own \n")
    print("(B).")
    print("-If you want to enter a regular expression and have our system print it to file ")
    print("Please enter the following into the cmd prompt: ")
    print("python ownExpr.py own --o \n")
    print("(C).")
    print("-If you want to enter a regular expression and include your name with output to file")
    print("Please enter the following into the cmd prompt: ")
    print("python ownExpr.py own --o --name (your Name)")
    print("Default name is Borris \n")
    print("(D).")
    print("-If you require help")
    print("Please enter the following into the cmd prompt: ")
    print("python ownExpr.py --h \n")
    print("(E).")
    print("-If you require help on running this program")
    print("Please enter the following into the cmd prompt: ")
    print("python help.py --help \n")
    print("**********************************************************")
      
def randExpr():
    print("**********************************************************")
    print("(A).")
    print("-To generate a random regular expression and string")
    print("Please enter the following into the cmd prompt: ")
    print("python randExpr.py rand \n")
    print("(B).")
    print("-If you want to generate random regular expressions and have our system print them to file ")
    print("Please enter the following into the cmd prompt: ")
    print("randExpr.py rand --o \n")
    print("(C).")
    print("-If you want to generate random regular expressions and include your name and output to file")
    print("Please enter the following into the cmd prompt: ")
    print("python randExpr.py rand --o --name (Your name)")
    print("Default name is Borris \n")
    print("(D).")
    print("-If you require help")
    print("Please enter the following into the cmd prompt: ")
    print("python randExpr.py --h \n")
    print("(E).")
    print("-If you require help on running this program")
    print("Please enter the following into the cmd prompt: ")
    print("python help.py --help \n")
    print("**********************************************************")
 

def helpMe():
    print("To get help on running this program enter into command line (python help.py --help)")

print("**********************************************************")
print(" Welcome to this regular expression engine!!!!!! \n")
while True:
    #Ask user if they want to use a pre-defined expression or enter their own
   
    print(" Please choose from the following options: \n")
    print("A. Do you want to enter your own expression? (Press A) ")
    print("B. Do you want to generate a random expression? (Press B)")
    print("C. Do you need Help? (Press C)")
    print("D. Do you want to exit this application? (Press E)")

    #setting up input variable
    choice = input()
    #the the user choose A then this will happen
    if choice =='A' or choice =='a':
        ownExpr()
        break

    elif choice =='B' or choice =='b':
        randExpr()
        break

    elif choice =='c' or choice =='C':
        helpMe()
        break

    elif choice =='e' or choice =='E':
        print("==============================================")
        print("Good-bye, Thanks for checking out this program!!!!\n")
        break

    if choice != 'a' or choice !='b' or choice != 'c' or choice != 'e'.casefold():
        print("**********************************************************")
        print("\n")
        print("Invalid selection entered, Please try again")
        print("**********************************************************")
        print("\n")


#Resources used
"""

code for taking input found on found on: 
https://www.geeksforgeeks.org/taking-input-in-python/

various python help
https://www.w3schools.com/python/python_operators.as

how to randomise variables
https://stackoverflow.com/questions/32288236/how-do-i-randomly-select-a-variable-from-a-list-and-then-modify-it-in-python

argparse tutorial
https://docs.python.org/3/library/argparse.html

How to save to file in python 
https://www.geeksforgeeks.org/reading-writing-text-files-python/

How to set default values to a name command line argument 
https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value

Name command line argument 
https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/

casefold()
https://www.programiz.com/python-programming/methods/string/casefold
"""