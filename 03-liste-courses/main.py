import sys


shopping_list = []
def add_item():
     item = input("Ajoutez un element a la liste ")
     shopping_list.append(item)
    
def remove_item():
     del_item = input("Supprimer un element de la liste ")
     if  del_item in shopping_list:
         shopping_list.remove(del_item)
     else:
         print("L'élément n'existe pas dans la liste. ")

def display_list():
     print(shopping_list)

def clear_list():
    shopping_list.clear()

while True:      

    print("1.Ajouter un élément a  la liste ")
    print("2.Retirer un élément de la liste ")
    print("3.Afficher la liste ")
    print("4.Vider la liste ")
    print("5.Quitter ")

    choice = input("Quel est votre choix ? ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_list()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        sys.exit()
    else:
        print("Entrez un nombre valide")
        
    