import sys

#Check for errors
if len(sys.argv) < 2:
    print ("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

#Print name tags
else:
    print("Hello, my name is", sys.argv[1])
