def get_text():
    while True:
        text = input("Enter a text: ")
        if text == "":
            print("Text is empty. Try again.")
        else:
            return text 