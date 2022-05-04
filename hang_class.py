class Hang:

    def __init__(self):
        self.points = 0
        self._word = ''
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                         'v', 'w', 'x', 'y', 'z']
        self.guessed_letter = []
        self.word_guessed = []
        self.listed_word = []

    def start_game(self):
        for i in self._word:
            self.word_guessed.append('_')
            self.listed_word.append(i)

    def set_word(self, word: str):
        self._word = word

    def get_word(self):
        return self._word

    def guess(self, letter: str):
        letter = letter.lower()
        word = self.get_word()
        if letter not in self.guessed_letter and letter not in self.alphabet:
            return print('Please enter valid response')
        if len(letter) > 1:
            return print('Please enter valid response')
        if letter in self.guessed_letter:
            return print('Please enter valid response')
        else:
            self.show(letter)
            self.guessed_letter.append(letter)
            self.alphabet.pop(self.alphabet.index(letter))
            if letter not in word:
                self.points += 1

    def show(self, letter):
        count = 0
        while count < len(self.listed_word):
            if self.listed_word[count] == letter:
                self.word_guessed[count] = letter
            count += 1
