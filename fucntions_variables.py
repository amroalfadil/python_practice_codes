#to create python folder qrite in terminal of the VScode code file_name.py
#print("hello, world")
#to run we need to use this command python file_name.py
#Functions : a verb let you do something in the programe, the function here is print()
#arguments :  input to the function influnace its behavior 
#bug: is a mistake in a programe
#print()
input("What's your name?")
print("Hello, world")
#but this dont print your name  when you run hello world
#we need to leverage "return values"
#variables can do this, to save value in  memory or a continer of a value
#Ask user for thier name
#say hello to user
"""
name = input("What is your name?")
print("hello,")
print(name)
"""

#comments : notes to your self on the code go on top and add a comment, can be also a todo list (pseudocode =to outline your programe in advance)
"""
this is a comment too
"""

#we can solve above programe in many ways
name = input("What is your name? ") # note we have space here after the question mark
#print("hello," + name) # but there is missing space you can "Hello, "
#print("hello, ", name) #when passing multiple arguments if apply space automatically
'''
print("hello, ", end="")
print(name)
'''
#print("hello, \""friend\"") escaping to pring qouts
#remove whitespace from str
name =name.strip()

#capitalise user's name (it does it for the only first letter)
name = name.capitalize()
#you can title every thing like this
name = name.title()
#you can chain functions togather to tide up the code
name = name.strip().title()
#or you can even combine it more
name = input("What is your name? ").strip().title()
print(f"hello, {name}") #formate string  or f-string
#we can clean the string in different ways (extra spaces , capetalisations...etc)
#you can extract a word from a string 
#split user's name into first name and last name 
first, last = name.splilte(" ")
print(f"hello, {first}")
#int = no decimal point 1,2,3,4,-1,-2,-3
# % mean modulo operator = take the remainder after dividing a number by another
#you can run python interactive mode by typing python in terminal and will see >>>



