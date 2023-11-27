def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        #print(i, end = " ") # for debugging to check temporary used can delete after finished
        #print("#" * (i+1)) #we added 1 to ensure starting from 1
        print("#" * (i+1)) # using the debugger in vs code
        reversed(print("#" * (i+1)))
if __name__ == "__main__":
    main()