import argparse
import regex
import random


def main():
    keepGoing = True
    while keepGoing:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "r", help="Generate a random expression from a bank of pre-defined expressions and string inputs", type=str)
        parser.add_argument(
            "-o", "--output", help="Output the results of your expression to file", action="store_true")
        print("******************************************************************")
        print("Do you want to generate a random expression and string? \n")
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
            print("Good-bye, Thanks for checking out this program!!!! \n")
            keepGoing = False
            break
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
                # if yes chosen the user will exit stuck loop and can enter a new expression
                if keepGoing == 'y' or keepGoing == 'Y':
                    stuck = False
                # if no chosen the loop will break
                elif keepGoing == 'N' or keepGoing == 'n':
                    print("\n")
                    print("==============================================")
                    print("Good bye, Thanks for checking out this program!!!!\n")
                    stuck = False
                else:
                    stuck = True
        # list of premade expressions
        exprList = ["a.b*", "a.b", "b", "a", "a*",
                    "b*", "b**", "a.b.b.c*", "a.c", "c"]
        # list of premade strings
        strList = ["bbbbbbbbbbbbbbb", "ab", "a", "b",
                   "aaaaaaaaaaaaaaaaaaaa", "abc", "ac", "c"]
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
        output = regex.match(expression, string1)
        # Output results
        print("output: ")
        print(regex.match(expression, string1))
        print("========================================================")
        args = parser.parse_args()
        if args.output:
            file = open("expression.txt", "a")
            file.write("The result of this random regular expression \n")
            file.write(str(expression) + '\n')
            file.write(str(string1) + '\n')
            file.write(str(output) + '\n')
            file.write(str("****************************") + '\n')
        print(args.r)


if __name__ == "__main__":
    main()
