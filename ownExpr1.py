import argparse
import regex


def main():
    keepGoing = True
    while keepGoing:

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "own", help="Enter your own expression and comparable string", type=str)

        print("******************************************************************")
        print("Please enter an expression and a string to compare it to.\n")
        print("Do you want to enter in an expression and string?\n")
        # if yes chosen the user can enter an expression
        keepGoing = input("Press Y for Yes or N for No \n")
        if keepGoing == 'y' or keepGoing == 'Y':
            keepGoing = True
         # if no chosen the loop will break
        elif keepGoing == 'N' or keepGoing == 'n':
            print("\n")
            print("==============================================")
            print("Good bye, Thanks for checking out this program!!!! \n")
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
                #if yes chosen the user will exit stuck loop and can enter a new expression
                if keepGoing == 'y' or keepGoing == 'Y':
                    stuck = False
                #if no chosen the loop will break 
                elif keepGoing == 'N' or keepGoing == 'n':
                    print("\n")
                    print("==============================================")
                    print("Good bye, Thanks for checking out this program!!!!\n") 
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
        print(regex.match(expression, stringinput))
        print("******************************************************************\n")
    args = parser.parse_args()
    print(args.own)


if __name__ == "__main__":
    main()

