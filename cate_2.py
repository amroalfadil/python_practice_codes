'''
for i in [0,1,2]:
    print("meow")
'''
# we can improve the designe by introducing a function range() it starts from 0
'''
for i in range(3):
    print("meow")
'''
# a pythonic way is to change the i to _ becuase it is not required variable because you dont care about the name 
'''
for _ in range(3):
    print("meow")
'''
#if you really to be pythonic , end = "" this to not end in blank line
#print("meow\n" * 3, end = "")
#we can recive a number from the user and be positive value, to match your expectation 
'''
n = int(input("what's n? "))
if n<0:
    n = int(input("what's n? "))
    if n<0
        n = int(input())......etc we can keep asking is it negative is it negative for ever
'''
'''
#better to do with a loop
while True:
    # we want to break from this infinit loop
    n = int(input("what's n? "))
    if n< 0:
        continue
    else:
        break
'''
'''
#more pythonic way
while True:
    n = int(input("what's n? "))
    if n > 0:
        break


for _ in range(n):
    print("meow")
'''

# we can have meow function

def main():
    #lets ask the user for a number lets invent another function called get_number()
    number = get_number()
    # then change the 3 to the value you recive from the user
    meow(number)

    # remmember this function still not exsist just creating the logic
def get_number():
    while True:
        # go a head and get number from the user and convert it to integer
        n = int(input("what's n? "))
        #then compare if positive
        if n >0:
            # you can break but you can return the value
            return n
    '''
    or you can do this above 
            break
        return n
    '''

def meow(n):
    for _ in range(n):
        print("meow")

main()