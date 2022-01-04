import os
import random
import time
from words import word_list
from hangmanimg import hangman_graphic


def load_game():
    """
    start screen for game
    """
    hangman_title()
    player_name = input('Welcome to Hangman! Enter your name to play ')
    os.system('clear')
    hangman_title()
    print('Hello', player_name, 'lets play hangman!')
    time.sleep(5)
    play_game()


def get_word():
    """
    gets random word from word list
    """
    word = random.choice(word_list)
    return word.upper()


def hangman_title():
    print("""
 
  _   _                                         
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/                       

 """)


def play_game():
    """
    logic for the main game
    """
    word = get_word()
    reveal = list(len(word)*'_')
    lives = 7
    game_won = False
    while game_won is False and lives > 0:
        os.system('clear')
        hangman_title()
        print(hangman_graphic[7 - lives])
        print(' '.join([str(e) for e in reveal]))
        print('you have', lives, 'lives left')
        guess = input('Guess a letter or a word: ').upper()
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
        os.system('clear')
        hangman_title()
        print(hangman_graphic[7])
        print('You failed, the word was', word)
    else:
        os.system('clear')
        hangman_title()
        print('You win! The word was', word)


load_game()