import sys

try:
    print("Hello, my name is", sys.argv[1]) #Se colocar o nome depois de python name.py, ele vai entender que a palavra no terminal, deverá ser impressa
except IndexError:
    print("Too few arguments")