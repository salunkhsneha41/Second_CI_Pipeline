def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(sentence.lower())

    return alphabet.issubset(letters)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    if is_pangram(sentence):
        print("The sentence is a Pangram.")
    else:
        print("The sentence is not a Pangram.")