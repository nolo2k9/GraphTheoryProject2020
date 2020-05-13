import argparse
import regex


def main():
    keepGoing = True
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "own", help="Enter your own expression and comparable string", type=str)
    parser.add_argument(
        "-o", "--output", help="Output the results of your expression to file", action="store_true")

    while keepGoing:

        print("******************************************************************")
        print("Do you want to enter in an expression and string?\n")
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
                    print("Good-bye, Thanks for checking out this program!!!!\n")
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
        output = regex.match(expression, stringinput)
        print(regex.match(expression, stringinput))
        print("******************************************************************\n")

    args = parser.parse_args()
    if args.output:
        file = open("expression.txt", "a")
        file.write("The result of this regular expression \n")
        file.write(str(expression) + '\n')
        file.write(str(stringinput) + '\n')
        file.write(str(output) + '\n')
        file.write(str("****************************") + '\n')
    print(args.own)


if __name__ == "__main__":
    main()
