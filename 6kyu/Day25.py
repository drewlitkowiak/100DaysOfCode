'''
https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python
Level: 6kyu


Directions:


Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  FalseWrite a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False


Tests:


import codewars_test as test

try:
	from solution import valid_braces
except: # function name used to be in camelCase
	from solution import validBraces as valid_braces

def assert_valid(string):
    test.assert_equals(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))

def assert_invalid(string):
    test.assert_equals(valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string))


@test.describe("Valid Braces")
def tests():
	@test.it("sample Tests")
	def sample_tests():
		assert_valid( "()" )
		assert_invalid( "(}" )
		assert_valid( "[]" )
		assert_invalid("[(])")
		assert_valid( "{}" )
		assert_valid( "{}()[]" )
		assert_valid( "([{}])" )
		assert_invalid( "([}{])" )
		assert_valid( "{}({})[]" )
		assert_valid( "(({{[[]]}}))" )
		assert_invalid( "(((({{" )
		assert_invalid( ")(}{][" )
		assert_invalid( "())({}}{()][][" )
'''

brace_pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def valid_braces(string):
    # Stack ftw
    brace_stack = []
    for char in string:
        
        # If valid opening bracket
        if char in brace_pairs:
            brace_stack.append(char)
        
        # If not approprate closing bracket
        elif len(brace_stack) == 0 or brace_pairs[brace_stack.pop()] != char:
            return False
        
    # Make sure all opening brackets have been closed
    return len(brace_stack) == 0

