def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    guess = input("Please enter a single alphabetical character: ")

    while not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character.")
        guess = input("Please enter a single alphabetical character: ")

    secret_word = "apple"
    if check_guess(guess, secret_word):
        return True
    else:
        return False

if __name__ == "__main__":
    while not ask_for_input():
        pass