def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def main():
    print("Palindrome Checker")
    while True: 
        word = input("Enter a word: ")
        if is_palindrome(word):
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()