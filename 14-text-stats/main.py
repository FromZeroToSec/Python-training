def get_text():
    """Ask the user to enter a non-empty text and return it"""
    while True:
        text = input("Enter a text: ").strip()
        if text == "":
            print("Text is empty. Try again.")
        else:
            return text