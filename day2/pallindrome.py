"""
125. Valid Palindrome
Easy
Topics
premium lock icon
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
import re

class Pallindrome:

    def is_pallindrome(self, s):
        # s1 = re.sub(r'[ ,.:]', '', s).lower()

        s1 = ''.join(filter(str.isalnum, s)).lower()
        return s1 == s1[::-1]
    

if __name__ == '__main__':
    sol = Pallindrome()
    val = sol.is_pallindrome(s='')
    print(val)

    val = sol.is_pallindrome(s='ala')
    print(val)

    val = sol.is_pallindrome(s='alasdfg')
    print(val)
