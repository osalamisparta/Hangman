from hang_class import Hang
from os import system
from sys import platform
p = ''
if platform == "win32":
    p = "win32"
    # Windows...
def clear(p):
   # for windows
   if p == 'win32':
      return system('cls')

   # for mac and linux
   else:
       return system('clear')




numbers = ['0','1','2','3','4','5','6','7','8','9','10']
print()
print()
print("WELCOME TO HANGMAN!")
print()
print()
print("Player 1, please input your word!")
print()
while True:
    word = input()
    if word.isalpha() == False or ' ' in word:
        print()
        print('Please enter a valid response!')
    else:
        clear(p)
        game = Hang()
        game.set_word(word)
        game.start_game()
        print()
        print('The game now starts!')
        print('If your score is more than 5 you lose!')
        print()
        clear(p)
        print('Player 2, now its your turn!')
        print()
        while True:
            print('Available letters: ')
            print(game.alphabet)
            print()
            print('Player two please guess a letter!')
            print()
            letter = input()
            game.guess(letter)
            print()
            print('Word: ', game.word_guessed)
            print('Score: ', game.points)
            print('You have guessed: ', game.guessed_letter)

            input('press enter to continue')
            clear(p)
            if game.points == 5:
                print()
                print('Player 2 you lose, Player 1 wins!')
                print('The word was: ',game.get_word())
                break
            if game.word_guessed == game.listed_word:
                print()
                print('Player 1 you lose, Player 2 wins!')
                print('The word was: ',game.get_word())
                break
        break
    break
print ('GAME OVER')





