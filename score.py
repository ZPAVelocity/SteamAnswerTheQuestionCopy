BIG_SCORE = 10
MIDDLE_SCORE = 5
SMALL_SCORE = 1
class Score(object):
    '''
    Score counter
    Offer functions to change score
    '''

    def __init__(self, initScore=0):
        self.score = initScore

    def add(self, addNum):
        self.score += addNum

    def minus(self, minusNum):
        self.score -= minusNum
