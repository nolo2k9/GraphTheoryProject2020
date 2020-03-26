**Graph Theory Project 2020**

```
This project aims to build a program that can execute regular expressions on
strings using an algorithm known as Thompson’s construction.

Thompson's construction algorithm, also called the McNaughton-Yamada-Thompson algorithm, is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA). This NFA can be used to match strings against the regular expression. 
```

**parser.py**
```
The parser.py script is where the code created inside regex.py gets parsed and the results are displayed to the screen.
When this script is run on the command line, the user is initially faced with two options. 

(1).
To run a predefined set of expressions and strings, which are randomised so the output will be different each time it's run. 
This was accomplished using random.choice(), and a list[] containing the various expressions. Then a variable was assigned to equal the output of this random function. 
The same was done for the string that was to be passed in to compare it against. Both variables are then passed into the match function, which analyzes the input

(2).
To enter in their expression and string of choice to compare against. This is accomplished using the input() function with a variable assigned to both the expression and the string. Both are then passed into the match function created in regex.py where they are analysed. Some basic user input validation is also used here to ensure that the correct inputs are used.
```

**test.py**
```
In this script, the various tests on the program are carried out. The required script is first imported so enable this script to run the code. The first test tests to see whether various expressions do or do not output the correct information when running against various strings. This ensures that the outputted information will always be correct when the program is running. The code is tested using the assert method. 
The assert method makes sure that the code being passed in does what the programmer intends it to do. In other words, it "asserts" the code. The test is then printed out using a print statement and displayed to the console. 

```

**regex.py**

***Classes***
```
The script regex.py contains the backbone of this project. At the top of the script contains the classes used in this project. 
(1).
The class State contains the edges and labels used. This is because all edges are labelled by a label and every state has 0,1 or 2 edges from it. 

(2). 
The class Fragment represents an NFA with a start and accepts state
```

***Functions***

**Shunt**
```
This function returns the infix regular expression in postfix notation.

Infix expression is a single letter, or an operator, proceeded by one infix string and followed by another infix string.
A
A + B
(A + B) + (C – D)

Postfix expression is a single letter or an operator, preceded by two postfix strings. Every postfix string longer than a single variable contains first and second operands followed by an operator.

A
A B +
A B + C D –

It specifies an order of precedence for the operators i.e '*' being the highest order of precedence '.' being the second-highest etc

It then loops through the input one character at a time analysing each entered character adding them to the list or popping them from the list.
This is achieved using the pop method and the append method.

pop()
pop()is an inbuilt function in Python that removes and returns last value from the list or the given index value.
append()
The append() method in python adds a single item to the existing list.

It then outputs the operators in order of precedence according to the rules of postfix notation. 

```


**compile**
```
This function returns an NFA fragment which represents the infix expression.
It firstly converts infix notation to postfix notation by making a variable equal to shunt with infix passed into it postfix = shunt(infix).

It then makes the variable postfix a stack of characters
, then an empty stack for NFA fragments is declared.

Using a while loop it then goes through the contents of postfix and depending on the character it will pop or accept the fragment. When it has gone through all of the characters it creates a new instance of fragment passing in the start and accepts states, the result is then returned. 

```

**follows**
```
This function adds a state to a set and follows all of the E arrows.
It takes in state and current as parameters.

If the state is not in the current state put that state into the current state.
It then checks if the state is labelled by an e, if it's not it will loop through the states pointed to by this state. 
Then follow all of their e arrows too add them to follows
```
**match**
```
This function will return true if the regular expression fully matches the entered string (according to the rules followed by Thompson's construction). It will otherwise return False declaring the expression and the string not equal.

It firstly compiles the regular expression into he needed NFA. 
It then tries to match the regular expression with the passed in string.
It then loops through the characters in the string provided and follows the arrows not labelled by e. Then if the label of the state is equal to the character read it will add then state at the end of the arow to the current set.
It will then return the results.
```


**How to use this project**
```
To compile and run the code written in the script 'regex.py' on your console window in the correct directory execute the statement (python parser.py).
Similarly, if you want to run the test script created for this project execute the command (python test.py).
```


***Information was taken from***

**Thompson Construction information**
```(https://en.wikipedia.org/wiki/Thompson%27s_construction)```

**Basic writing and formatting syntax**
```https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax```

**Expressions**
```http://www.studyalgorithms.com/theory/what-are-infix-postfix-and-prefix-expressions/```

**Appened() definition**
```https://towardsdatascience.com/append-in-python-41c37453400```

**POP() definition**
```https://www.geeksforgeeks.org/python-list-pop/```

