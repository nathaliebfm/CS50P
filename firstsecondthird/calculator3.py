def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

#A mesma coisa do calculator 2, mas a função pow (power) já faz a o número elevado ao valor indicado
def square(n):
    return pow(n, 2)

main()