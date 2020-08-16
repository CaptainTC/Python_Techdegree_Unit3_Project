import random
import string
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase('In God we Trust'),
            Phrase('The sky is blue'),
            Phrase('I want to learn to code'),
            Phrase('Did I do a good job'),
            Phrase('I want to live forever')]
        self.active_phrase = None
        self.guesses = []

    def start_game(self):
        self.welcome()
        info = self.get_random_phrase()
        while self.missed < 5 and info.check_complete():
            info.diplay()
            true_value = (info.check_letter(self.get_geuss().lower()))
            self.missed += true_value
            if true_value == 1:
                print('\n\nYou have {} out of 5 lives remaining!\n\n'.format(5 - self.missed))
            info.check_complete()
        self.game_over()

    def get_random_phrase(self):
        return self.phrases[random.randint(0, 4)]

    def welcome(self):
        space = ' ' * 30
        line = '=' * 30
        print(space + line + '\n   {}Welcome to Phrase Hunter\n'.format(space) + space + line)

    def get_geuss(self):
        alphabet = string.ascii_lowercase
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
            space = ' ' * 30
            line = '=' * 30
            print(space + line + "\n   {}Unfortantly You have Lost.\n".format(space) + space + line)
        else:
            space = ' ' * 30
            line = '=' * 30
            print(space + line + "\n{}Congradulations You've Won!!!!\n".format(space) + space + line)
        while True:
            again = input("\nWould you like to play again? (Y/N): ")
            if again.lower() == 'y':
                break
            elif again.lower() == 'n':
                print('\nThank you for playing')
                break
            else:
                print("Please enter 'y' or 'n': ")
        if again.lower() == 'y':
            game = Game()
            game.start_game()
