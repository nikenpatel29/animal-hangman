# The random library selects a random item from a list
import random
# The time library uses real-world time in the program
import time

# Introduce the game and ask for their name 
print("\nThe Animal Hangman Challenge by NikenP\n")
name = input("What is your name? ")

# The sleep method delays the program for a few seconds
print("Hello " + name + "!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)

# Define the main function 
def main():

    # Global allows the scope to expand from a local variable to a variable used outside the function
    global word
    global length
    global count
    global display
    global guessed
    global play_game

    # Defines the global variables and the animals that will be guessed in the game
    animals = ["dog","cat","squirrel","dolphin","shark","frog","lion","tiger","monkey","lizard","horse", "rabbit", "raccoon", "cow", "chicken", "elephant", "sheep"]
    word = random.choice(animals)
    length = len(word)
    count = 0
    display = '_' * length
    guessed = []
    play_game = ""

# A function that takes in the "play_game" argument for either allowing the user to play again or stop
def play_again():
        global play_game
        play_game = input("Do you want to play again? y = yes, n = no \n")
        while play_game not in ["y", "n"]:
            play_game = input("Do You want to play again? y = yes, n = no \n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Thanks for playing!")
            exit()

# A function that contains the arguments necessary for the user to effectively play the game
def game():
    global word
    global count
    global display
    global guessed
    global play_game

    # Sets a limit on how many times the user can guess a word
    limit = 5

    # Asks for user input for their answer, while also removing the letter from the given word from display
    guess = input("This is the word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    # Checks to see if no input was given, the length of the input was 2 letters or more at once, or the input was a number, which would all force a retry
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, type one letter at a time\n")
        game()

    # The extend method will add the guessed word to the empty list of guesses
    elif guess in word:
        guessed.extend([guess])

        # An index variable is created that uses the find method to search for the letter in the word if it is correct
        index = word.find(guess)

        # Slices the index to add the letters to the spot that it belongs in the word or the index itself
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    # If a correct letter has already been guessed, then user will be prompted to try a different letter to guess
    elif guess in guessed:
        print("Try another letter.\n")

    # If an incorrect letter is guessed by the user, the count of errors is increased by 1, which contributes to the limit of 5
    else:
        count += 1

        # 1st incorrect guess. The hangman appears with every count, which is corresponded with how many guesses are left. 
        if count == 1:

            # The time.sleep() function is used again to delay the program for a suspenseful display of the hangman
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
            # The mathematical calculation of limit-count tells how many guesses remain for the user
            print("Wrong. " + str(limit - count) + " guesses remaining\n")

        # 2nd incorrect guess, starts to show a rope
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong. " + str(limit - count) + " guesses remaining\n")


        # 3rd incorrect guess, rope lengthens
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong. " + str(limit - count) + " guesses remaining\n")


        # 4th incorrect guess, head begins to show and the user is warned to be very careful for their final guess
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong. Be very careful from here on. " + str(limit - count) + " last guess remaining\n")


        # 5th incorrect guess, so there are no guesses left and the body is fully shown, indicating that the user has lost.
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong! YOU LOSE!\n")

            # Tells the user what the correct word was after showing the user's correct guesses, if there were any
            print("The word was:",guessed,word)
            play_again()


    # If the word was guessed correctly with all of the included letters, the user is congratulated
    if word == '_' * length:
        print("Let's go! You are correct!")

        # The play_again() function asks the user to play again by calling that defined function
        play_again()
    
    # If the wrong guesses is not equal to the limit, then the game continues
    elif count != limit:
        game()

# Calling these functions executes the entire code
main()
game()
