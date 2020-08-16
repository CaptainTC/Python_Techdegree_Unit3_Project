import re

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.original_phrase = phrase
        list_of_words = re.findall(r'([\b\w]+)', phrase)
        new_phrase = []
        value = 0
        for _ in range(len(list_of_words)):
            underscore = len(list_of_words[value])
            num_us = underscore * '_'
            new_phrase.append(num_us)
            value += 1
        self.active_phrase = ' '.join(new_phrase)

    def diplay(self):
        display = list(self.active_phrase)
        print('\n' + " ".join(display))

    def check_letter(self, guess):
        if guess in self.original_phrase.lower():
            count = self.phrase.lower().count(guess)
            self.phrase = list(self.phrase)
            self.active_phrase = list(self.active_phrase)
            for _ in range(count):
                try:
                    location = self.phrase.index(guess.upper())
                    letter = None
                except:
                    location = self.phrase.index(guess)
                    letter = "lower"
                del self.phrase[location:(location+1)]
                del self.active_phrase[location:(location+1)]
                self.phrase.insert(location, "#")
                if letter ==  "lower":
                    self.active_phrase.insert(location, guess)
                else:
                    self.active_phrase.insert(location, guess.upper())
            self.phrase = "".join(self.phrase)
            self.active_phrase = "".join(self.active_phrase)
            return 0
        else:
            return 1

    def check_complete(self):
        if self.original_phrase.lower() == self.active_phrase.lower():
            if len(self.phrase) == len(self.active_phrase):
                the_phrase = list(self.original_phrase)
                print('\n', " ".join(the_phrase), '\n')
                self.phrase = self.phrase  + "Extended - Random_Data"
            return False
        else:
            return True
