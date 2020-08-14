import re
import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
        'In God we Trust',
        'The sky is blue',
        'I want to learn to code',
        'Did I do a good job',
        'I want to live forever']
        self.original_phrase = None
        self.active_phrase = None
        self.guesses = []

    def start_game(self):
        self.welcome()
        self.get_random_phrase()
        info = Phrase(self.original_phrase, self.active_phrase)
        while self.missed < 5 and info.check_complete(self.original_phrase):
            info.diplay()
            self.missed += (info.check_letter(self.get_geuss().lower(), self.original_phrase))
            info.check_complete(self.original_phrase)
        self.game_over()

    def get_random_phrase(self):
        self.original_phrase = self.phrases[random.randint(0, 4)]
        list_of_words = re.findall(r'([\b\w]+)', self.original_phrase)
        new_phrase = []
        value = 0
        for _ in range(len(list_of_words)):
            underscore = len(list_of_words[value])
            num_us = underscore * '_'
            new_phrase.append(num_us)
            value += 1
        self.active_phrase = ' '.join(new_phrase)


    def welcome(self):
        space = ' ' * 30
        line = '=' * 30
        print(space + line + '\n   {}Welcome to Phrase Hunter\n'.format(space) + space + line)

    def get_geuss(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while True:
            ans = input('\n\nGuess a letter: ')
            if len(ans) == 1 and ans.lower() in alphabet:
                if ans.lower() in self.guesses or ans.upper() in self.guesses:
                    print("You've guessed this character already.")
                    continue
                break

            else:
                print('Please enter only 1 alphabetical character.')
        self.guesses.append(ans)
        return ans

    def game_over(self):
        if self.missed == 5:
            print('\n', self.original_phrase)
            space = ' ' * 30
            line = '=' * 30
            print(space + line + "\n   {}Unfortantly You have Lost.\n".format(space) + space + line)
        else:
            print('\n', self.original_phrase)
            space = ' ' * 30
            line = '=' * 30
            print(space + line + "\n{}Congradulations You've Won!!!!\n".format(space) + space + line)
        while True:
            again = input("Would you like to play again? (Y/N): ")
            if again.lower() == 'y':
                break
            elif again.lower() == 'n':
                print('Thank you for playing')
                break
            else:
                print("Please enter 'y' or 'n': ")
        if again.lower() == 'y':
            game = Game()
            game.start_game()
