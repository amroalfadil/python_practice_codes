x = int(input("What is the maximum number you would like?")).strip()
def printer(counter):
    for count in range(counter):
        print("*"*count)
    for count in reversed(range(counter)):
        print("*"*count)
printer(x)