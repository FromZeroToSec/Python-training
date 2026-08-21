
def main():
    a = 0
    b = 1
    compteur = 0
    while compteur < 10:
        print(a)
        old_a = a
        a = a + b
        b = old_a
        compteur = compteur + 1


if __name__ == "__main__":
    main()