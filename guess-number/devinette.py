import random

while True:
    secret = random.randint(1, 10)
    attempts = 0

    while attempts < 5:
        guess = int(input("Veuillez choisir un chiffre entre 1 et 10: "))
        attempts += 1

        if guess == secret:
            print("You win")
            break
        elif guess > secret:
            print("Trop grand")
        elif guess < secret:
            print("Trop petit")
    else:
        print(f"Perdu le chiffre secret est {secret}")

    again = input("Rejouer ? (y/n)").lower()
    if again == "n":
        break