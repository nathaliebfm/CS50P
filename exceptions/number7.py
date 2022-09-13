def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass #Você pega o erro, mas não avisa o usuário o que aconteceu, só continua no loop


main()