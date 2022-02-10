'''
https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
Level: 8kyu


Directions

Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".


Test

import codewars_test as test
from solution import greet

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
        test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
'''

def greet(name):
    return f"Hello, {name} how are you doing today?"
