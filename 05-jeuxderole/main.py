from random import randint 

# Statistiques du joueur et de l'ennemi
mypv = 50
ennemypv = 50
potion = 3
skip = False

print("⚔️ Le Combat Commence ⚔️ ")

# Boucle de jeu - tourne tant que les deux joueurs sont en vie
while mypv > 0 and ennemypv > 0:
    
# Si le joueur a utilisé une potion au tour précédent, il passe son tou
    if skip :
        ennemyattack = randint(5,15)
        mypv -= ennemyattack
        print(f"iMPOSSIBLE D'ATTAQUER ! Vous avez subit {ennemyattack} point de degat !⚔️ \n Il vous reste {mypv} point de vie ❤️")
        print ("-" * 50) 
        if mypv <= 0:
            print(" YOU LOSE❌")
            break
        skip = False
        continue
    
# Le joueur choisit son action
    choice = int(input("Souhaitez-vous attaquer 🗡️ (1) ou utiliser une potion 🧪(2) ? "))

# Option 1 - Attaque
    if choice == 1:
        myattack = randint(5,10)
        ennemypv -= myattack
        print(f"Vous avez infligé {myattack} point de degat a l'ennemie !⚔️")
        if ennemypv <= 0:
            print("🎊YOU WIN🎊")
            break

# Option 2 - Utiliser une potion        
    elif choice == 2:
        if potion > 0:
            skip = True
            heal = randint(15, 50)
            mypv += heal
            potion -= 1
            if mypv > 50 :
                mypv = 50 
            print(f"Vous récupérez {heal} point de vie ❤️ (Il vous reste {potion} potion 🧪")
        else :
            print("Acune potion disponible 🛑") 
            continue

# L'ennemi attaque si il est encore en vie        
    if ennemypv > 0:
        ennemyattack = randint(5,15)
        mypv -= ennemyattack
        print(f"Vous avez subit {ennemyattack} point de degat !⚔️ \n Il vous reste {mypv} point de vie ❤️\n Il reste {ennemypv} points de vie a l'ennemie.")
        if mypv <= 0:
            print(" YOU LOSE❌")
            break
        print ("-" * 50) 