#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Keith Nolan

#imports
import argparse
import regex

#main method
def main():
    #keepgoing loop control variable
    keepGoing = True
    #defining argparse to a variable + Description
    parser = argparse.ArgumentParser(
        description='Create your own regular expressions')
    #adding an argument of type str name is own with help message
    parser.add_argument(
        "own", help="Enter your own expression and comparable string", type=str)
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
    print("Hi {}, Lets get started!".format(args["name"]))

    #while keepgoing
    while keepGoing:

        print("*************************************************************************")
        #asking if user wants to enter in expression and string witht heir name or default name 
        print("Do you want to enter in an expression and string, {}? \n".format(
            args["name"]))

        # if yes chosen the user can enter an expression
        keepGoing = input("Press Y for Yes or N for No \n")

        if keepGoing == 'y' or keepGoing == 'Y':
            keepGoing = True

         # if no chosen the loop will break
        elif keepGoing == 'N' or keepGoing == 'n':
            print("\n")
            print("===============================================================================")
            print("{} you opted to print your regular expression to file. \n".format(args["name"]))
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
                    print(
                        "Good-bye {}, Thanks for checking out this program!!!! \n".format(args["name"]))
                    stuck = False
                else:
                    stuck = True
                    
        print("\n")
        print("******************************************************************")
        print("Please enter an expression and a string to compare it to.\n")
        expression = input("Enter expression : \n")
        print("\n")
        print("Expression entered: " + expression + "\n")
        print("******************************************************************\n")
        stringinput = input("Enter string : \n")
        print("\n")
        print("String entered  : " + stringinput + "\n")
        print("Your entered expression is: ")
        #setting users name to a variable 
        name = ("{}").format(args["name"])
        #defining output for printing to file
        output = regex.match(expression, stringinput)
        #print results
        print(regex.match(expression, stringinput))
        print("******************************************************************\n")

     #setting up arguments to be parsed
    args = parser.parse_args()
    #if user opts to have their expression output to file
    if args.output:
        print("Printing your expressions and results to file........\n")
        #open file 
        file = open("expression.txt", "a")
        #write name and following message
        file.write(str(name +', The results of your regular expression are: ' + '\n'))
        file.write("The results of your regular expression are \n")
        #write exprssion
        file.write(str(expression) + '\n')
        #write their inputted string
        file.write(str(stringinput) + '\n')
        #write output 
        file.write(str(output) + '\n')
        file.write(str("****************************") + '\n')
    


if __name__ == "__main__":
    main()
