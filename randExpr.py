#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Keith Nolan

#imports
import argparse
import regex
import random

#main method
def main():
    #keepgoing loop control variable
    keepGoing = True
    #defining argparse to a variable + Description
    parser = argparse.ArgumentParser(
            description='Generate random regular expressions')
     #adding an argument of type str name is own with help message
    parser.add_argument(
            "rand", help="Generate a random expression from a bank of pre-defined expressions and string inputs", type=str)
     #adding an argument of type str name is output, shortcut of o with help message store value set to true
    parser.add_argument(
            "-o", "--output", help="Output the results of your expression to file", action="store_true")
    #adding an argument of type str name is name shortcut --n with help message and defualt name set to borris
    parser.add_argument("-n", "--name", nargs='?', type=str,
                        help="name of the user", default='Borris')

    print("\n")
    print("***************************** WELCOME ***********************************")
     #setting up arguments to be parsed
    args = vars(parser.parse_args())
    #print name
    print("Hi {}, Lets get started!\n".format(args["name"]))
     #while keepgoing
    while keepGoing:

        print("*************************************************************************")
        args = vars(parser.parse_args())
        #asking if user wants to enter in expression and string witht heir name or default name 
        print("Do you want to generate a random expression and string, {}? \n".format(args["name"]))
       
        # if yes chosen the user can enter an expression
        keepGoing = input("Press Y for Yes or N for No \n")

        if keepGoing == 'y' or keepGoing == 'Y':
            keepGoing = True

         # if no chosen the loop will break
        elif keepGoing == 'N' or keepGoing == 'n':
            print("\n")
            print("==============================================")
            print("If you opted to print your regular expression to file. \n")
            print(
                "In the current directory you are in, type the following into the cmd prompt: \n")
            print("On Mac or Linux: (ls) then (cd expression.txt) then (ls) \n")
            print("On Windows: (dir) then (cd expression.txt) then (ls) \n")
            print("Good-bye {}, Thanks for checking out this program!!!! \n".format(args["name"]))
            keepGoing = False
            break

        else:
            #if user makes wrong selection
            stuck = True
            while stuck:
                print("\n")
                print("==============================================")
                print("\n")
                print("Wrong selection entered!!! \n")
                print("Do you want to enter another expression? \n")
                print("==============================================")
                keepGoing = input("Press y for yes or n for no \n")
                # if yes chosen the user will exit stuck loop and can enter a new expression
                if keepGoing == 'y' or keepGoing == 'Y':
                    stuck = False
                # if no chosen the loop will break
                elif keepGoing == 'N' or keepGoing == 'n':
                    print("\n")
                    print("==============================================")
                    print("Good-bye {}, Thanks for checking out this program!!!! \n".format(args["name"]))
                    stuck = False
                else:
                    stuck = True

        #list of premade expressions
        exprList = ["a.b*", "b", "a","a|b*","b*|c*","a|b|c","a*|b*|c*",
                    "b*", "b.c*", "a.c", "c","a|c", "a*", "c*"]

        #list of premade strings
        strList = ["bbbbbbbbbbbbbbb", "ab", "a", "b","abbbbbbbbbbb","bcccccccc","bc",
                   "aaaaaaaaaaaaaaaaaaaa", "abc", "ac", "c","ccccccccccccccccccccccc","b","c","a"]

        # assigning a variable to a random string in the list using random.choice()
        expression = random.choice(exprList)

        # assigning a variable to a random string in the list using random.choice()
        string1 = random.choice(strList)

        print("\n")
        print("========================================================")
        print("A random expression and string have been chosen.......calculating........")
        print("\n")
        print("========================================================")

        # Output contents of expression variable
        print("The random expression chosen was: " + expression + "\n")
        # Output contents of string1 variable
        print("The random string choesen was: " + string1 + "\n")
        #defining output for printing to file
        output = regex.match(expression, string1)
        #setting users name to a variable 
        name = ("{}").format(args["name"])
        # Output results
        print("output: ")
        #print results
        print(regex.match(expression, string1))
        print("========================================================\n")

        args = parser.parse_args()
        #if user opts to have their expression output to file
        if args.output:
            print("Printing your expressions and results to file........\n")
            #open file 
            file = open("expression.txt", "a")
            #write name and following message
            file.write(str(name +', The results of this randomly geneated regular expression are: ' + '\n'))
            #write exprssion
            file.write(str(expression) + '\n')
            #write their inputted string
            file.write(str(string1) + '\n')
            #write output 
            file.write(str(output) + '\n')
            file.write(str("****************************") + '\n')
       


if __name__ == "__main__":
    main()
