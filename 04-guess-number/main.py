import random

while True:
    print("😎Le jeu du nombre mystere😎")
    secret = random.randint(1,100)
    attemps = 0 
    tentative = 5 
    while attemps < 5:
        try: 
            nombre = int(input("Devine le chiffre: "))
            attemps += 1
            tentative -= 1
            if secret == nombre:
                print(f"""Bravo le nombre mytere etait bien {secret} !
                    Tu as trouver le nombre en {attemps} tentatives ! """)
                break
            elif secret > nombre:
                print(f"""Le nombre mystere est plus grand que {nombre} !
                Attention il te reste que {tentative} tentative ! """)
            elif secret < nombre:
                print(f"""Le nombre mystere est plus petit que {nombre} !
                Attention il te reste que {tentative} tentative ! """)
        except ValueError:
            print("Entre un nombre valide.")
    else:
        print(" Vous avez perdu ! ") 
        break
    again = input("Rejouer ? (y/n)").lower()
    if again == "n":
        break