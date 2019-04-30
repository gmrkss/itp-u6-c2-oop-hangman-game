from .exceptions import *


class GuessAttempt(object):
    def __init__(self, attempt, hit=None, miss=None):
        self.attempt = attempt
        self.hit = hit
        self.miss = miss
        if (self.hit==True and self.miss==True) or (self.hit==False and self.miss==False):
            raise InvalidGuessAttempt
        
    def is_hit(self):
        if self.hit:
            return True
        return False
    
    def is_miss(self):
        if self.miss:
            return True
        return False

class GuessWord(object):
    def __init__(self, answer, masked=None):#, guess=GuessAttempt()):
        self.answer = answer
        self.masked = len(self.answer)*"*"
#         self.guess = guess
        if self.answer=='':
            raise InvalidWordException

    def perform_attempt(self, attempt):
        if len(attempt)>1:
            raise InvalidGuessedLetterException
        
            
        

class HangmanGame(object):
    pass
