from .exceptions import *
import random

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
        self.answer = answer.lower()
        self.masked = len(self.answer)*"*"
        self.attempt = GuessAttempt(attempt, hit=None, miss=None)
        if self.answer=='':
            raise InvalidWordException

    def perform_attempt(self, attempt):
        attempt = attempt.lower()
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
        
        else:
            setattr(self.attempt, 'hit', False)
            setattr(self.attempt, 'miss', True)
            
            return self.attempt

class HangmanGame(object):
    def __init__(self, list_of_words, number_of_guesses=5, remaining_misses=5):
        self.list_of_words = list_of_words
        self.number_of_guesses = number_of_guesses
        self.remaining_misses = number_of_guesses
    
    def select_random_word(self):
        if self == []:
            raise InvalidListOfWordsException
        return random.choice(self)
        
    def start_new_game(self):
        select_random_word(self)
        if self == []:
            raise InvalidListOfWordsException
        
        
        
    
    
    def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
