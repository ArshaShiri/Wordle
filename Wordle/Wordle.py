class Wordle:
    def __init__(self, word):
        self.answer = word.lower()
        self.answerLength = len(self.answer)
        self.numberOfTries = 6
        self.letterCount = {}

        self.countUniqueLettersOfAnswer()

    def countUniqueLettersOfAnswer(self):
        for letter in self.answer:
            self.letterCount[letter] = self.letterCount.get(letter, 0) + 1

    def takeAGuess(self, guess):
        self.numberOfTries = self.numberOfTries - 1
        result = ""

        for letter in guess:
          result = result + "-"

        return result

myFirstGame = Wordle("Hello")
print(myFirstGame.answerLength)