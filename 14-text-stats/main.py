#Étape 3 — compter les mots : une fonction qui split le texte et compte les mots.
#Étape 5 — fréquence des mots : comme dans word-counter, mais réutilisée ici.
#Étape 6 — ratio mots/phrases : calcul simple, division.
#Étape 7 — README + nettoyage.


def get_text():
    """Ask the user to enter a non-empty text and return it"""
    while True:
        text = input("Enter a text: ").strip()
        if text == "":
            print("Text is empty. Try again.")
        else:
            return text
        
def count_characters(text):
    """Return the number of characters in the text"""
    return len(text)