# Author: Keith Nolan
#run the regex file 
#import the regex script
import regex

#https://www.geeksforgeeks.org/taking-input-in-python/
expression = input ("Enter expression :") 
print("Expression entered: " + expression) 
name1 = input("Enter string : ") 
print("String entered  : " + name1) 

print (regex.match(expression, name1))