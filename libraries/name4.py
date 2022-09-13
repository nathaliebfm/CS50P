import sys


if len(sys.argv) < 2:
    sys.exit ("Too few arguments")

for name in sys.argv[1:]: #These brackets slice off the first tag, which would print "Hello, my name is name4.py"
#Since I don't know the length of the list, I won't put a second number after:
    print("Hello, my name is", name)
