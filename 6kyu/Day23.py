'''
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
Level: 6kyu


Directions:


Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]


Test:


test.assert_equals(up_array([2,3,9]), [2,4,0])
test.assert_equals(up_array([4,3,2,5]), [4,3,2,6])
test.assert_equals(up_array([1,-9]), None)
'''

def up_array(arr):
    # Sanity check input
    # arr must be populated with positive single digit integers
    if len(arr) == 0 or any(elem < 0 or elem > 9 for elem in arr):
        return None
    # Iterate starting from ones place
    for index, elem in reversed(list(enumerate(arr))):
        elem += 1
        if elem == 10:
            # Carry the one
            arr[index] = 0
        else:
            arr[index] = elem
            return arr
    # Carry the one on a list full of nines
    arr.insert(0, 1)
    return arr

