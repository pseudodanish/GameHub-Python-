# Hangman Game
class Demo:
    def play_hangman(self):
        words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
        word = random.choice(words)
        guessed = []
        attempts = 6

        print("\n\nWelcome to Hangman!")
        print("The word has", len(word), "letters.")

        while attempts > 0:
            print("\n\nAttempts left:", attempts)
            display_word = ""
            for letter in word:
                if letter in guessed:
                    display_word += letter
                else:
                    display_word += "_"
            print(display_word)

            if display_word == word:
                print("Congratulations! You have guessed the word!")
                break

            guess = input("Enter a letter: ")
            if guess in guessed:
                print("You have already guessed this letter.")
                continue
            guessed.append(guess)

            if guess not in word:
                attempts -= 1
                print("The letter is not in the word.")
            else:
                print("The letter is in the word.")

        if attempts == 0:
            print("You have run out of attempts. The word was:", word)  
            
    
