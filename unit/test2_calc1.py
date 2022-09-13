from calc1 import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4 #dessa forma reduz a linhas de código, aí o programador tem que procurar o porquê deu o assertionerror
    except AssertionError: #Então para não ter dúvidas, manda o programa imprimir o motivo do erro
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()