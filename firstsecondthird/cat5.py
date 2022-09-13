while True: #Você cria um looping infinito, até o usuário colocar a informação que você quer
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")