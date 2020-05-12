import regex 
import unittest

'''
Special variable understood by python, basically asks is this file being ran directly by python or being imported
'''
if __name__ == "__main__":
#list of tests
    tests =[
            ["a.b|b*", "bbbbbbbb", True],
            ["a.b|b*", "bbx", False],
            ["a.b", "ab", True],
            ["b**", "b", True],
            ["b*", "ababa", False],
            ["b**", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", True],
        ]
    


    
   
#for loop to run tests
for test in tests:
    '''
    assert is they keyword used to run tests eg assert that a = a
    asserting that the expressions and the strings match the statements True or false
    '''
    assert regex.match(test[0], test[1]) == test[2],test[0] + ("should " if test[2] else "should not ") + " match " + test[1]
    #Printing out results
    print(regex.match(test[0], test[1]) == test[2],test[0] + (" should " if test[2] else " should not ") + " match " + test[1])






  