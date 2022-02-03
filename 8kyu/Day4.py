'''
https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
Level 8kyu

Directions

When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.

Test

import codewars_test as test
from solution import switch_it_up

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(switch_it_up(0), "Zero")
        test.assert_equals(switch_it_up(9), "Nine")

Function
'''

number_reference = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

def switch_it_up(number):
    return number_reference[number]
    
