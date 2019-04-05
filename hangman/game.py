from .exceptions import *


class GuessAttempt(object):
    def __init__(self, attempt, hit, miss):
        self.attempt = attempt
        self.hit = hit
        self.miss = miss


class GuessWord(object):
    pass


class HangmanGame(object):
    pass
