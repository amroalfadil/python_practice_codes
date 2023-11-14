'''
x = input("what's x? ")
y = input("what's y? ")
#not because we ask for user input it is str not in or a number 
# we need to add a function to make them a number by using int()
z = int(x) + int(y)

print(z)
'''
#we can modify the code to be better , by nesting functions int(input())
x = int(input("what's x? "))
y = int(input("what's y? "))
# we can use float() too instead of integers to accept from the user
# you can round numbers to the nearest integer round()
#look at the documention round(number[, ndigits])  [] brackets means options which is the number of digits you would like to round too 10th place or 100th place
x = float(input("what's x? "))
y = float(input("what's y? "))
#what if we want to print in certine system by using comma , or ' or .
#z= roud(x+y) lets use division
z = round(x/y, 2) #round to 2 dicimal places 
#print(f"{z:,}")
# or can be used like this to round number print(f"{z:.2f}") this will round to the 2 dicemal places
print(z)