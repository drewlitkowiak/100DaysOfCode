'''
https://www.codewars.com/kata/598106cb34e205e074000031/train/python
Level: 6kyu


Directions:


Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats

ex2 P O~ O~ ~O O~ has 1 deaf rat

ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats


Tests:


test.it("ex1")
test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)
  
test.it("ex2")
test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)
  
test.it("ex3")
test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)
'''

def count_deaf_rats(town):
    deaf_counter = 0
    # Remove spaces
    town = town.replace(' ', '')
    # Split on where the piper is
    piper_left, piper_right = town.split('P')
    # For all rats left of the piper
    for i in range(0, len(piper_left), 2):
        if piper_left[i:i+2] == 'O~':
            deaf_counter += 1
    # For all rats right of the piper
    for i in range(0, len(piper_right), 2):
        if piper_right[i:i+2] == '~O':
            deaf_counter += 1
    return deaf_counter
    
