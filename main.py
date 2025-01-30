class Dictionary:

    def __init__(self, words):
        self.words = set(words)
    
    def getRandomWord(self):
        pass

    def isWordInDictionary(self):
        pass


class Wordle:

    dictionary = Dictionary(["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"])

    MAX_TURNS = 5

    def __init__(self):
        self.turns = 0
        self.solution = self.dictionary.getRandomWord()

    def guess(self, word):
        pass

    def hint(self, word):
        pass