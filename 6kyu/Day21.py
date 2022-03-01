'''
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
Level: 6kyu

Directions:


Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.



Test:


import codewars_test as test
from solution import high

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")
'''

def high(x):
    word_score = lambda x: sum([ord(char)-96 for char in x])
    words = x.split()
    highest_scoring_word = words[0]
    highest_word_score = word_score(highest_scoring_word)
    for word in words[1:]:
        if ( score := word_score(word) ) > highest_word_score:
            highest_word_score = score
            highest_scoring_word = word
    return highest_scoring_word

