import random

class Dictionary:

    def __init__(self, words):
        self.words = set(words)
    
    def getRandomWord(self):
        return random.choice(list(self.words))

    def isWordInDictionary(self, word):
        return word in self.words


class Wordle:

    dictionary = Dictionary(["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"])

    MAX_TURNS = 5

    WINNER = "You got it! Amazing!"

    TRY_AGAIN = "Wrong guess!"

    SHOW_HINT = "Hint: "

    GAME_OVER = "You're out of turns, game over!"

    INPUT_STRING = "Please enter your first guess: "

    def __init__(self):
        self.turns = 0
        self.solution = self.dictionary.getRandomWord()
        self.wordHint = []

    def guess(self, word):
        
        if not self.dictionary.isWordInDictionary(word):
            return False
        
        self.turns += 1
        
        if self.solution == word:
            return True
        else:
            self.hint(word)
            return False

        

    def hint(self, word):
        
        tempHint = ["-"]*len(self.solution)

        letters = [0]*26

        for char in self.solution:
            letters[ord[char] - ord("a")] +=1
        

        for i in range(len(word)):
            if self.solution[i] == word[i]:
                if letters[ord[word[i]] - ord("a")] > 0:
                    tempHint[i] = "1"
                    letters[ord[word[i]] - ord("a")] -= 1
                    
        
        for i in range(len(word)):
            if word[i] in self.solution:
                if letters[ord[word[i]] - ord("a")] > 0:
                    tempHint[i] = "0"
                    letters[ord[word[i]] - ord("a")] -= 1
        
        self.wordHint = tempHint

        self.SHOW_HINT = f"Hint: {"".join(tempHint)}"

        

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
        print(wordle.SHOW_HINT)

    if wordle.turns >= wordle.MAX_TURNS:
        print(wordle.GAME_OVER)

if __name__ == "__main__":
    main()