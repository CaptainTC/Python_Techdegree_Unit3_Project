class Phrase:
    def __init__(self, phrase, active_phrase):
        self.phrase_copy = phrase
        self.active_phrase_copy = active_phrase
        self.lives = 5

    def diplay(self):
        print('\n' + self.active_phrase_copy)

    def check_letter(self, guess, original):
        if guess in original.lower():
            count = self.phrase_copy.lower().count(guess)
            self.phrase_copy = list(self.phrase_copy)
            self.active_phrase_copy = list(self.active_phrase_copy)
            for _ in range(count):
                try:
                    location = self.phrase_copy.index(guess.upper())
                    letter = None
                except:
                    location = self.phrase_copy.index(guess)
                    letter = "lower"
                del self.phrase_copy[location:(location+1)]
                del self.active_phrase_copy[location:(location+1)]
                self.phrase_copy.insert(location, "#")
                if letter ==  "lower":
                    self.active_phrase_copy.insert(location, guess)
                else:
                    self.active_phrase_copy.insert(location, guess.upper())
            self.phrase_copy = "".join(self.phrase_copy)
            self.active_phrase_copy = "".join(self.active_phrase_copy)
            return 0
        else:
            self.lives -= 1
            print('\n\nYou have {} out of 5 lives remaining!\n\n'.format(self.lives))
            return 1

    def check_complete(self, original_phrase):
        if original_phrase.lower() == self.active_phrase_copy.lower():

            return False
        else:
            return True
