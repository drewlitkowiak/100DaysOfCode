'''
https://www.codewars.com/kata/56ed20a2c4e5d69155000301/train/python
Level: 7kyu

Directions:


You are given a string of n lines, each substring being n characters long. For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

Example: a = "abcd\nefgh\nijkl\nmnop"
scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
Printed:

abcd   ----->   aabbccdd
efgh            aabbccdd
ijkl            aabbccdd
mnop            eeffgghh
                eeffgghh
                eeffgghh
                iijjkkll
                iijjkkll
                iijjkkll
                mmnnoopp
                mmnnoopp
                mmnnoopp
Task:
Write function scale(strng, k, v) k and v will be positive integers. If strng == "" return "".


Test:


def testing(actual, expected):
    test.assert_equals(actual, expected)

test.describe("scale")
test.it("Basic tests")
a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
testing(scale(a, 2, 3), r)
testing(scale("", 5, 5), "")
testing(scale("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH")
'''

def scale(strng, k, v):
    if not strng:
        return ''
    
    vertical_scale = []
    for i in strng.split('\n'):
        
        horizontal_scale = []
        for j in i:
            horizontal_scale.append(j*k)
        
        vertical_scale += [''.join(horizontal_scale)]*v
    
    return '\n'.join(vertical_scale)
