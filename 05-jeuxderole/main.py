from random import randint

# Statistiques initiales du joueur et de l'ennemi
MYPV = 50
ENNEMYPV = 50
POTION = 3
skip = False

print("⚔️ Le Combat Commence ⚔️")

# Boucle de jeu - tourne tant que les deux joueurs sont en vie
while MYPV > 0 and ENNEMYPV > 0:
    # Si le joueur a utilisé une potion lors du tour précédent, il passe son tour
    if skip:
        enemy_attack = randint(5, 15)
        MYPV -= enemy_attack
        print(f"IMPOSSIBLE D'ATTAQUER ! Vous avez subi {enemy_attack} point(s) de dégât ! ⚔️ Il vous reste {MYPV} point(s) de vie ❤️")
        print("-" * 50)
        if MYPV <= 0:
            print("YOU LOSE❌")
            break
        skip = False
        continue

    # Demande d'action à l'utilisateur
    try:
        choice = int(input("Souhaitez-vous attaquer 🗡️ (1) ou utiliser une potion 🧪 (2) ? "))
    except ValueError:
        print("Entrée invalide. Veuillez saisir 1 ou 2.")
        continue

    # Option 1 - Attaque
    if choice == 1:
        player_attack = randint(5, 10)
        ENNEMYPV -= player_attack
        print(f"Vous avez infligé {player_attack} point(s) de dégât à l'ennemi ! ⚔️")
        if ENNEMYPV <= 0:
            print("🎊YOU WIN🎊")
            break

    # Option 2 - Utiliser une potion
    elif choice == 2:
        if POTION > 0:
            skip = True
            heal = randint(15, 50)
            MYPV += heal
            POTION -= 1
            if MYPV > 50:
                MYPV = 50
            print(f"Vous récupérez {heal} point(s) de vie ❤️ (Il vous reste {POTION} potion(s) 🧪)")
        else:
            print("Aucune potion disponible 🛑")
            continue
    else:
        print("Choix non valide, veuillez réessayer.")
        continue

    # L'ennemi attaque si il est encore en vie
    if ENNEMYPV > 0:
        enemy_attack = randint(5, 15)
        MYPV -= enemy_attack
        print(f"Vous avez subi {enemy_attack} point(s) de dégât ! ⚔️\nIl vous reste {MYPV} point(s) de vie ❤️\nIl reste {ENNEMYPV} point(s) de vie à l'ennemi.")
        if MYPV <= 0:
            print("YOU LOSE❌")
            break
        print("-" * 50)