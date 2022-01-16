"""
imports
"""
import os  # operating system functionality
import random  # random for randomising words
import time  # control when a line of code in used
import string
from words import word_list  # list of hangman wordss
from hangmanimg import hangman_graphic  # hangman graphic for game
alphabet = list(string.ascii_uppercase)


def load_game():
    """
    start screen for game
    """
    hangman_title()
    print('Welcome to Hangman! \n')
    print('Guess the word by inputting letters before the lives run out. \n')
    print('You can only guess one letter at a time. \n')
    print('If the lives reach 0, the game is over. \n')
    print('Good Luck! \n')
    # checks the user has entered an alphabetic letter for name
    while True:
        player_name = input('Enter your first name to play:\n')
        if player_name.isalpha():
            break
        else:
            print("Please use letters only, try again\n")
    # clears the terminal
    os.system("cls" if os.name == "nt" else "clear")
    hangman_title()
    print('Hello', player_name, 'lets play hangman!')
    # timer for welcome message
    time.sleep(4)
    play_game()


def get_word():
    """
    gets random word from word list
    """
    word = random.choice(word_list)
    return word.upper()


def hangman_title():
    """
    hangman title to print
    """
    print(
        """

  _   _
 | | | |  __ _  _ __    __ _  _ __ ___    __ _  _ __
 | |_| | / _` || '_ \\  / _` || '_ ` _ \\  / _` || '_ \\
 |  _  || (_| || | | || (_| || | | | | || (_| || | | |
 |_| |_| \\__,_||_| |_| \\__, ||_| |_| |_| \\__,_||_| |_|
                       |___//

        """
    )


def play_game():
    """
    logic for the main game
    """
    # starting variables
    word = get_word()
    reveal = list(len(word)*'_')
    lives = 7
    game_won = False
    guesses = []
    # logic to run game
    while game_won is False and lives > 0:
        os.system("cls" if os.name == "nt" else "clear")
        hangman_title()
        print(hangman_graphic[7 - lives] + '\n')
        print(' '.join([str(e) for e in reveal]) + '\n')
        print('You have', lives, 'lives left\n')
        print('You have used: ', ", ".join(guesses) + '\n')
        # checks user has put in one letter at a time and not repeated
        while True:
            guess = input('Guess a letter:\n').upper()
            if guess not in alphabet:
                print('Invalid input, please enter a letter\n')
            elif guess in guesses:
                guess = print('You already guessed ' + guess + ' guess again ')
            else:
                break
        guesses.append(guess.upper())
        if guess == word:
            game_won = True
        if len(guess) == 1 and guess in word:
            for i in range(0, len(word)):
                letter = word[i]
                if guess == letter:
                    reveal[i] = guess
            if '_' not in reveal:
                game_won = True
        else:
            lives -= 1
    # if the user loses
    if lives == 0:
        os.system("cls" if os.name == "nt" else "clear")
        hangman_title()
        print(hangman_graphic[7]+'\n')
        print('You failed, the word was', word + '\n')
        reset_game()
    else:
        # if the user wins
        os.system("cls" if os.name == "nt" else "clear")
        hangman_title()
        print('You win! The word was', word + '\n')
        reset_game()


def reset_game():
    """
    restart the game after user has won or lost
    """
    restart_game = False
    # asks the user if they want to replay
    while restart_game is False:
        restart = input('Do you want to play again? Enter Y or N:\n').upper()

        if restart == 'Y':
            restart_game = True
            play_game()

        elif restart == 'N':
            restart_game = True
            print('Thank you for playing, goodbye!')
            os.system("cls" if os.name == "nt" else "clear")
            load_game()
        else:
            print('Please enter Y or N')


load_game()
