#first print the blocks
'''
print("#")
print("#")
print("#")
'''
#lets improve using for loop
'''
for _ in range(3):
    print("#")
'''
# lets write function more dynamic
def main():
    print_column(3)

def print_column(height):
    #for _ in range(height):
        #print("#")
    # another way to print
    print("#\n" * height, end="")

main()

#lets now print the ? marks for the coin 
def main():
    print_row(4)

def print_row(width):
    #for _ in range(width):
        #print("?")
    # another way to print
    print("?" * width)

main()

# if we would like to build the grid in mario 

def main():
    print_square(3)


def print_square(size):
    #for each row in square
    for i in range(size):
        # more improved version instead of below
        print("#" * size)
        # for each brick in row
        #for j in range(size):

            #Print brick
            #print("#", end = "")
        # below the inner loop outsider of the out loop, because i don't want a new line after,
        #each brick
        #print()

main()

