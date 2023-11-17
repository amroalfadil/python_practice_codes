def main():
    x = int(input("What is x? "))
    #you invent a function to keep the logic is_even(x)
    if is_even(x):
        print("Even")
    else:
        print("Odd")
#build the invented function earlier
def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False





main()