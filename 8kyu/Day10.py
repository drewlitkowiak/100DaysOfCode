'''
https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
Level: 8kyu

Directions


Write a function that checks if a given string (case insensitive) is a palindrome.

Test


@test.describe('sample tests')
def sample_tests():
    test.assert_equals(is_palindrome('a'), True)
    test.assert_equals(is_palindrome('aba'), True)
    test.assert_equals(is_palindrome('Abba'), True)
    test.assert_equals(is_palindrome('malam'), True)
    test.assert_equals(is_palindrome('walter'), False)
    test.assert_equals(is_palindrome('kodok'), True)
    test.assert_equals(is_palindrome('Kasue'), False)
'''

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
