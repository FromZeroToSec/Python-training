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


def get_top_words(word_count, n):
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_count[:n] 


def display_results(top_words):
    for word, count in top_words:
        print(f"{word}: {count}")


def main():
    text = get_text()
    word_count = count_words(text)
    top_words = get_top_words(word_count, 5)
    display_results(top_words)

if __name__ == "__main__":
    main()