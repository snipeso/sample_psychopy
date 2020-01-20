class Scorer:
    def __init__(self):
        self.scores = {
            "missed": 0,
            "correct": 0,
            "incorrect": 0,
            "tot": 0,
            "extraKeys": 0,
        }

    def getScore(self):
        print("+++++++++++++++++++++++++++++++++++++++++++")
        for key in self.scores.keys():
            self._printScore(key, self.scores[key])

        print("+++++++++++++++++++++++++++++++++++++++++++")

    def _printScore(self, name, score):
        print(name, score)
