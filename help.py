import argparse


print("\n")
print("***********************************************************************************************************************")
print("                                             WELCOME TO THE HELP PAGE")
parser = argparse.ArgumentParser()
parser.add_argument("help", 
help= print("***********************************************************************************************************************"
"\n This program was developed to tell you if an inputted string is a regular expression or not. \n"
"\n You have two options which are: \n"
"\n (1) To generate a random regular expression from a bank of premade regular expressions. \n"
"\n (2) Enter in your own regular expression and then a string which you want to compare it to. \n"
"\n This program also enables you to print your results to file and enter your name. \n"
"\n The program will then inform you if the randomly generated expression or your own expression is infact a regular expression or not. \n"
"\n An example of a regular expression and comparable string is A|B* BBBBBBBBBBBBBBBBB \n"
"\n Regular expression operators: \n"
"\n (.) A.B  \n"
"\n Both A and B must only be present in the output for it to be true \n"
"\n Input -> A.B String -> AB   \n"
"\n (|) A|B  \n"
"\n  A or B must only be present in the output for it to be true \n"
"\n Input -> A|B String -> A/B   \n"
"\n (*) A.B*  \n"
"\n Both A and B or multiple B's must only be present in the output for it to be true \n"
"\n Input -> A.B* String -> ABBBBBBBBBBBBB/AB   \n"
"\n Please Re-Run (python home.py) on the command line to get started \n"
"\n***********************************************************************************************************************"))
args = parser.parse_args()   
print (args)
