def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
   
#def get_int():
def get_int(prompt):
    while True:  #to make loop for ever
        try:
            return int(input(prompt))
            #return int(input("What's x? "))
            #x = int(input("What's x? "))
            #return x
        except ValueError:
            pass #ignoring the error and staying in the loop
            #print("x is not an integer")
        #else:
            #return x # return stronger than break so we delete break and add return below else:

main()