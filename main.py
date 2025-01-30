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

    WINNER = "You got it! Amazing!"

    TRY_AGAIN = "Wrong guess!"

    GAME_OVER = "You're out of turns, game over!"

    INPUT_STRING = "Please enter your first guess: "

    def __init__(self):
        self.turns = 0
        self.solution = self.dictionary.getRandomWord()

    def guess(self, word):
        pass

    def hint(self, word):
        pass


def main():

    wordle = Wordle()
    print(f"Welcome to Word Guess! You have {wordle.MAX_TURNS} turns to guess the word. ")


    while wordle.turns < wordle.MAX_TURNS:
        attempt = input(wordle.INPUT_STRING).lower()

        result = wordle.guess(attempt)

        if result:
            print(wordle.WINNER)
            break
        
        print(wordle.TRY_AGAIN)
    

    if wordle.turns >= wordle.MAX_TURNS:
        print(wordle.GAME_OVER)
