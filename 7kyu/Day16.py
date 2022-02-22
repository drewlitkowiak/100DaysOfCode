'''
https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python
Level: 7kyu

Directions:

You are going to be given a word. Your job will be to make sure that each character in that word has the exact same number of occurrences. You will return true if it is valid, or false if it is not.

For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"

The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.

Examples
"abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
"abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!
"123abc!" is a valid word because all of the characters only appear once in the word.


Test:

test.assert_equals(validate_word("abcabc"),True)
test.assert_equals(validate_word("Abcabc"),True)
test.assert_equals(validate_word("AbcabcC"),False)
test.assert_equals(validate_word("AbcCBa"),True)
test.assert_equals(validate_word("pippi"),False)
test.assert_equals(validate_word("?!?!?!"),True)
test.assert_equals(validate_word("abc123"),True)
test.assert_equals(validate_word("abcabcd"),False)
test.assert_equals(validate_word("abc!abc!"),True)
test.assert_equals(validate_word("abc:abc"),False)
'''

def validate_word(word):
    count_dict = {}
    for i in word.lower():
        count_dict[i] = 1 + count_dict.get(i, 0)
    occurences = set(count_dict.values())
    return len(occurences) == 1
