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
    def __init__(self, answer, masked=None, attempt=None):
        self.answer = answer
        self.masked = len(self.answer)*"*"
        self.attempt = GuessAttempt(attempt, hit=None, miss=None)
        if self.answer=='':
            raise InvalidWordException

    def perform_attempt(self, attempt):
        if len(attempt)>1:
            raise InvalidGuessedLetterException
        
        if attempt in self.answer:
            answer_word_chars=[]
            masked_word_chars=[]
            for char in self.answer:
                answer_word_chars.append(char)
            for char in self.masked:
                masked_word_chars.append(char)

            for index, char in enumerate(answer_word_chars):
                if char==attempt:
                    masked_word_chars[index]=attempt

            self.masked=''.join(masked_word_chars)    
            
            setattr(self.attempt, 'hit', True)
            setattr(self.attempt, 'miss', False)
            
            return self.attempt


class HangmanGame(object):
    pass
