'''
https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python
Level: 7kyu

Directions:

Your job is to implement a function which returns the last D digits of an integer N as a list.

Special cases:
If D > (the number of digits of N), return all the digits.
If D <= 0, return an empty list.
Examples:
N = 1
D = 1
result = [1]

N = 1234
D = 2
result = [3, 4]

N = 637547
D = 6
result = [6, 3, 7, 5, 4, 7]


Tests:


test.describe('Example tests')
test.assert_equals(solution(1,1),[1])
test.assert_equals(solution(123767,4),[3,7,6,7])
test.assert_equals(solution(0,1),[0])
test.assert_equals(solution(34625647867585,10),[5,6,4,7,8,6,7,5,8,5])

test.describe('d <= 0')
test.assert_equals(solution(1234,0),[])
test.assert_equals(solution(24134,-4),[])

test.describe('d > number of digits in n')
test.assert_equals(solution(1343,5),[1,3,4,3])
'''

def solution(n,d):
    if d <= 0:
        return []
    return [ int(x) for x in list(str(n))[-d:] ]

