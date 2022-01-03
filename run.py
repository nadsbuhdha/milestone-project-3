# import random
# from words import word_list

# def get_word():
#    word = random.choice(word_list)
#    return word.upper()

# print('get_word')


# def hangman_title():
#    print("""
#  _   _                       
# | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# |  _  | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                    |___/                 
# """)


# def main():
#    hangman_title()

# main()

def play_game():
    word = 'hangman'
    word = word.upper()
    reveal = list(len(word)*'_')
    lives = 7
    game_won = False
    while game_won is False and lives > 0:
        print(reveal)
        print('you have', lives, 'goes left')
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
        if game_won:
            print('You win')
        else:
            print('You failed, the word was', word)

    
play_game()