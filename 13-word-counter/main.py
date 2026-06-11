def get_text():
    while True:
        text = input("Enter a text: ")
        if text == "":
            print("Text is empty. Try again.")
        else:
            return text 
        
def count_words(text):
    word_count = {}
    for word in text.lower().split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count