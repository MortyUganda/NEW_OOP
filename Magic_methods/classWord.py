# Let's call any sequence of one or more Latin letters a word.

#  Implement the Word class that describes a word. When creating an instance, the class should accept one argument:

# word — the word
# An instance of the Word class should have the following formal string representation:

# Word('<the original word>')

 
# And the following informal string representation:

# <the word with the first letter capitalized and all other letters lowercase>

 
# Also, instances of the Word class must support all comparison operations using the operators 
# ==, !=, >, <, >=, and <=. Two words are considered equal if their lengths are the same. 
# A word is considered greater than another word if its length is longer.

from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word) -> None:
        self.word = word

    def __repr__(self) -> str:
        return f'''Word('{self.word}')'''
    
    def __str__(self) -> str:
        return f'{self.word.capitalize()}'
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented


print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))


