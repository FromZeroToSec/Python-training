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

def count_words(text):
    """Return the number of words in the text"""
    return len(text.split())
    
def count_sentences(text):
    """Return the number of sentences in the text"""
    return text.count(".") + text.count("?") + text.count("!")

def get_word_frequency(text):
    """Return a dictionary where keys are words and values are their frequency"""
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def get_word_per_sentence(word_count, sentence_count):
    """Return the average number of words per sentence"""
    if sentence_count == 0:
        return 0
    else:
        return word_count / sentence_count