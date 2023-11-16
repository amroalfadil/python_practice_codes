def printer(counter):
    for count in range(counter):
        print("*"*count)
    for count in reversed(range(counter)):
        print("*"*count)
printer(5)