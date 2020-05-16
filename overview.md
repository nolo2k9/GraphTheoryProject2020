Introduction 
This repository contains a regular expression engine. Which is built using an algorithm called Thompsons construction. Thompsons construction is a method of transforming a regular expression into an equivalent NFA (Nondeterministic finite automata). A regular expression is entered in or generated followed by a string to compare to the regular expression. The application then outputs a True or False statement indicating whether the entered expression and comparable string is in fact a regular expression when executed together.
I will now discuss the various files and features that are included in this application and explain how each of them work. 
home.py
The file home.py is meant to act like a main menu or, in the context of a game or other application this would be the first screen you see upon opening the application. It acts as a guide to the user of the application on what they can do and how they can achieve the results they are looking for. The layout was developed with simplicity and ease of use in mind to allow any user to navigate the various features this application has to offer with ease and without having to feel like they have to spend a lot of time learning how to use it. 
Upon running home.py the user is faced with the following options
 
Each of these options is clearly laid out in an easy to understand manner with each selection bringing the user to a different part of the application or allowing them to exit the application. If for example the user presses A it will bring them to a new set of instructions informing them how they can enter in their own regular expressions. 
 
Each clearly laid out instruction informs them of how they can achieve everything from simply entering in their own regular expression, entering their own expression and printing it to a file to entering their name to get a more personalized experience from using this program.
 If the user presses B when in this menu, they get a similar set of instructions but instead of options about entering in their own expressions it gives them options to execute a file where the system will generate random expressions and comparable strings for them. This was built with learning in mind so the user can get a better grasp of how regular expressions work, what expressions work with what strings and what does not work. When the user can visualize what is happening, I think it will help them understand more of how the whole process works.
 

Pressing C in this main menu will instruct the user about how to get help running this application should they need it. Below is an image of what instructions are produced if C is press on this options menu. 
Finally pressing E will exit this menu and stop the program. This is because the menu is built with a while loop. This was done to stop users entering in invalid options such as pressing x. This gives more control to the program and stops it from crashing if an invalid option is entered. 
The menu itself is designed simply each option for example (A) has a method that is fired upon pressing this button in either higher or lower case this is achieved using the casefold() method. Depending on what option is press depends on what method is fired. Any invalid selections will cause the loop to continue, where any correct options pressed will follow with a break from the loop and firing of the associated method. 
The methods themselves just contain well laid out text informing the user of how to use the selected function and what commands to run to achieve their desired output or result. 

ownExpr.py

![](C:\Users\Keith\Desktop\home.jpg)

