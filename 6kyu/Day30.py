'''
https://www.codewars.com/kata/559536379512a64472000053/train/python
Level: 6kyu


Directions:


Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

shift each letter by a given number but the transformed letter must be a letter (circular shift),
replace each digit by its complement to 9,
keep such as non alphabetic and non digit characters,
downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
reverse the whole result.
Example:
your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?



Tests:



test.assert_equals(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")

test.assert_equals(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2), 
    "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")
'''

def play_pass(s, n):
    # Convert everything to an ascii character
    string_ascii = [ord(c) for c in s]
    
    # Get ascii values for numbers and letters
    zero_ascii = ord('0')
    nine_ascii = ord('9')
    
    a_ascii = ord('a')
    z_ascii = ord('z')
    
    A_ascii = ord('A')
    Z_ascii = ord('Z')
    
    # The difference between lowercase and uppercase values
    lower_upper_diff = a_ascii - A_ascii
    
    for index, char in enumerate(string_ascii):
        
        # If it is lower case
        if a_ascii <= char <= z_ascii:
            # Caesar Ciper the letter
            char = ((char - a_ascii + n) % 26) + a_ascii
            # If it is in an even position, convert it to upper case
            if index % 2 == 0:
                char -= lower_upper_diff
            # Assign value to array
            string_ascii[index] = char
            
        # If it is upper case
        elif A_ascii <= char <= Z_ascii:
            # Caesar Cipher the letter
            char = ((char - A_ascii + n) % 26) + A_ascii
            # If it is in an odd position, convert it to lower case
            if index % 2 == 1:
                char += lower_upper_diff
            # Assign value to array
            string_ascii[index] = char
        
        # If it is a number
        elif zero_ascii <= char <= nine_ascii:
            # Then get the complemennt
            string_ascii[index] = 105 - char
    
    # Reverse the string and convert it back from an array ascii values
    return ''.join([chr(x) for x in reversed(string_ascii)])

