'''
https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python
Level: 7kyu

Directions:


Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"


Test:

import codewars_test as test
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'), 'alpha beta gamma delta alpha beta gamma delta');
'''

def remove_consecutive_duplicates(s):
    input = s.split()
    output = input[0:1]
    for x in input[1:]:
        if x != output[-1]:
            output.append(x)
    return ' '.join(output)
