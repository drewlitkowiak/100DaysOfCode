'''
https://www.codewars.com/kata/59b11f57f322e5da45000254/train/python
Level: 7kyu

Directions:


The Ones' Complement of a binary number is the number obtained by swapping all the 0s for 1s and all the 1s for 0s. For example:

ones_complement(1001) = 0110
ones_complement(1001) = 0110
For any given binary number,formatted as a string, return the Ones' Complement of that number.


Test:


test.assert_equals(ones_complement("0"), "1")
test.assert_equals(ones_complement("1"), "0")
test.assert_equals(ones_complement("01"), "10")
test.assert_equals(ones_complement("10"), "01")
test.assert_equals(ones_complement("1101"), "0010")
'''

def ones_complement(binary_number):
    return ''.join([str(int(not int(x))) for x in str(binary_number)])
