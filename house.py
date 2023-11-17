'''
using match 
task: we will create a programe asking the user for thier name
and output what house to be in in the world of harry potter
'''

name = input("What's your name? ")
'''
if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''
'''
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''

'''
match name:
    case "Harry": 
        print("Griffindor")
    case "Hermione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    # finally to handle other cases  use _:
    case _:
        print("Who?")
'''
# Or equeveleant to |
match name:
    case "Harry" | "Hermione" |  "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    # finally to handle other cases  use _: catch all.
    case _:
        print("Who?")