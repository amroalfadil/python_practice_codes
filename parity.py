def main():
    x = int(input("What is x? "))
    #you invent a function to keep the logic is_even(x)
    if is_even(x):
        print("Even")
    else:
        print("Odd")
#build the invented function earlier
'''
    is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
'''
# you can combine above as follows (pythonic way)
'''
    is_even(n):
    return True if n % 2 == 0 else False
'''
# even more improvement
def is_even(n):
    return (n % 2 == 0)




main()