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

word = 'hangman'
reveal = list(len(word)*'_')
print(reveal)
lives = 7
gameWon = False

while gameWon is False and lives > 0:
    guess = input('Guess a letter or a word: ')
    guess = guess

    if guess == word:
        gameWon = True
    else:
        lives -= 1


if gameWon:
    print('You win')
else:
    print('You failed, the word was', word)