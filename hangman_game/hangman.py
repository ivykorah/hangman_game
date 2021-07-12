import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
stages = hangman_art.stages

print(hangman_art.logo)

# keep track of the number of lives left.
#Set 'lives' to equal 6 initially.
lives = 6

# to test the code, uncomment the below code
# print(f"Pssst! The word is {chosen_word}")

#Create blanks for each letter in chosen_word
display = []
for alph in chosen_word:
    display.append("_")

#Check guessed letter
end_of_game = False
print(stages[6])

while end_of_game == False:
    guess = input("Please guess a letter from a to z:\n")

    # If the user has entered a letter they've guessed previously, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")

  #Check guessed letter
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = guess

  # If a wrong letter is entered, decrease life by one until no more life then loop ends
    if  guess not in chosen_word:
        lives -= 1
        image = stages[lives]
        print(image)
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life. You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("Game ends. You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters and end the game.
    if "_" not in display:
        end_of_game = True
        print("Game ends. You win.")
