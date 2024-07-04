import random
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'ice cream', 'jackfruit', 'kiwi', 'lemon', 'ango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'trawberry', 'tangerine', 'ugli fruit', 'victoria plum', 'watermelon', 'xigua', 'yellow passionfruit', 'zucchini', 'abundance', 'bouquet', 'cascade', 'daffodil', 'elegance', 'flamenco', 'giggle', 'hazard', 'iguana', 'jubilee', 'kaleidoscope', 'luminescent', 'elody', 'narrative', 'oceanic', 'patchwork', 'quartz', 'ebellion', 'apphire', 'tactile', 'ubiquitous', 'vibrant', 'wisteria', 'xenon', 'yonder', 'zestful', 'acacia', 'bougainvillea', 'calla', 'dahlia', 'echinacea', 'foxglove', 'gardenia', 'heliotrope', 'iris', 'jasmine', 'kalanchoe', 'larkspur', 'arigold', 'nasturtium', 'oleander', 'petunia', 'quaking grass', 'radish', 'weetpea', 'tansy', 'umbrella plant', 'violet', 'waxflower', 'xanthium', 'yarrow', 'zinnia']

def hangman():
    word = random.choice(words)
    guessed = ['_'] * len(word)
    incorrect_guesses_allowed = 6
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print("You have", incorrect_guesses_allowed, "chances to guess the word.")

    while True:
        print(' '.join(guessed))
        guess = input("Guess a letter: ").lower()
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            incorrect_guesses += 1
            print("Incorrect! You have", incorrect_guesses_allowed - incorrect_guesses, "chances left.")
        if '_' not in guessed:
            print(' '.join(guessed))
            print("Congratulations! You won!")
            break
        if incorrect_guesses == incorrect_guesses_allowed:
            print("Game over! The word was", word)
            break

if __name__ == "__main__":
    hangman()