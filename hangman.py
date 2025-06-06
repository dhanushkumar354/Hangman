import random
word_list = ['apple', 'banana', 'grape', 'orange', 'mango']
word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses allowed.\n")
while incorrect_guesses < max_incorrect:
    
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'
    
    print('Word:', ' '.join(display_word))
  
    if display_word == word:
        print("\n Congratulations! You guessed the word:", word)
        break
   
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic letter.\n")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
   
    elif guess in word:
        print(" Correct guess!\n")
        guessed_letters.append(guess)
    
    else:
        print(" Wrong guess.\n")
        incorrect_guesses += 1
        guessed_letters.append(guess)
    
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
    print("Guessed letters:", ' '.join(guessed_letters))
    print("--------------------")


if incorrect_guesses == max_incorrect:
    print("\n Sorry, you lost. The word was:", word)

print("\nThanks for playing Hangman!")
