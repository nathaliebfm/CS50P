def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass #Você pega o erro, mas não avisa o usuário o que aconteceu, só continua no loop


main()