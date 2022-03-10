'''
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
Level: 6kyu


Directions:


You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)


Tests:


test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
'''

def find_outlier(integers):
    # Check if it is odd/even
    first_bit = integers[0] & 0x1
    # Check if the second matches the first
    if integers[1] & 0x1 != first_bit:
        # If it doesn't then the tiebreaker is the third
        return integers[1] if (integers[2] & 0x1) == first_bit else integers[0]
    # Otherwise we can iterate through the rest
    for num in integers[2:]:
        if num & 0x1 != first_bit:
            return num

