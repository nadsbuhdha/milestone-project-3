import os
import random
import time
from words import word_list
from hangmanimg import hangman_graphic
import string
alphabet = list(string.ascii_uppercase)


def load_game():
    """
    start screen for game
    """
    hangman_title()
    print('Welcome to Hangman! \n')
    print('Guess the word by inputting letters before the lives run out. \n')
    while True:
        player_name = input('Enter your name to play:\n')
        if player_name.isalpha():
            break
        else:
            print("Please use only letters, try again")
    os.system("cls" if os.name == "nt" else "clear")
    hangman_title()
    print('Hello', player_name, 'lets play hangman!')
    time.sleep(4)
    play_game()


def get_word():
    """
    gets random word from word list
    """
    word = random.choice(word_list)
    return word.upper()


def hangman_title():
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
    word = get_word()
    reveal = list(len(word)*'_')
    lives = 7
    game_won = False
    guesses = []
    while game_won is False and lives > 0:
        os.system("cls" if os.name == "nt" else "clear")
        hangman_title()
        print(hangman_graphic[7 - lives] + '\n')
        print(' '.join([str(e) for e in reveal]) + '\n')
        print('You have', lives, 'lives left\n')
        print('You have used: ', ", ".join(guesses) + '\n')
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

    if lives == 0:
        os.system("cls" if os.name == "nt" else "clear")
        hangman_title()
        print(hangman_graphic[7])
        print('You failed, the word was', word)
        reset_game()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        hangman_title()
        print('You win! The word was', word)
        reset_game()


def reset_game():
    """
    restart the game after user has won or lost
    """
    restart_game = False

    while restart_game is False:
        restart = input('Do you want to play again? Enter Y or N:\n').upper()

        if restart == 'Y':
            restart_game = True
            play_game()

        elif restart == 'N':
            restart_game = True
            print('Thank you for playing, goodbye!')
            load_game()
        else:
            print('Please enter Y or N')


load_game()