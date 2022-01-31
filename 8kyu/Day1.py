'''
https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python
Level 8kyu

Directions

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. 
If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a
 series!'. If there are no good ideas, as is often the case, return 'Fail!'.

Test

import codewars_test as test
from solution import well

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')

Function
'''

def well(x):
    #your code here
    good_ideas = x.count('good')
    if good_ideas:
        if good_ideas > 2:
            return "I smell a series!"
        else:
            return "Publish!"
    else:
        return "Fail!"
