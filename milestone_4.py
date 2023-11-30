import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)
            self.num_letters -= 1
            return True
        else:
            self.num_lives -= 1
            print(f"Oops! {guess} is not in the word. You have {self.num_lives} lives left.")
            return False

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single alphabetical character: ")

            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue

            is_valid_guess = self.check_guess(guess)

            if is_valid_guess:
                break

            print("You already tried that letter!")

        self.list_of_guesses.append(guess)

    def update_word_guessed(self, guess):
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

    def print_game_status(self):
        print("Word:", " ".join(self.word_guessed))
        print("Guesses left:", self.num_lives)
        print("Guesses:", ",".join(self.list_of_guesses))

    def play_game(self):
        while self.num_lives > 0 and self.num_letters > 0:
            self.ask_for_input()
            self.print_game_status()

            if self.num_letters == 0:
                print("Congratulations! You won the game!")
            elif self.num_lives == 0:
                print("Sorry, you lost the game.")
                print(f"The word was {self.word}.")


if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grape", "strawberry"]
    game = Hangman(word_list)
    game.play_game()