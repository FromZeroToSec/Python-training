def normalize(word):
    return word.lower().replace(" ", "")


def is_anagram(word1, word2):
    return sorted(normalize(word1)) == sorted(normalize(word2))


def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    if is_anagram(word1, word2):
        print(f"{word1} and {word2} are anagrams.")
    else:
        print(f"{word1} and {word2} are not anagrams.")


if __name__ == "__main__":
    main()