def printer(counter):
    for count in range(counter):
        print("*"*counter)

        for count in refersed(range(counter)):
            print("*"count)

        printer(5)