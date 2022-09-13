import sys

# sys.exit: checks for errors, print the argument and exit the program
if len(sys.argv) < 2:
    sys.exit ("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])
