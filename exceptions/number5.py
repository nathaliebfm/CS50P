def main():
    x = get_int()
    print(f"x is {x}")

def get_int(): #jeito mais difícil
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main()