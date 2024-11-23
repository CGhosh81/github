"""Reversing an integer means to reverse all its digits.
•	For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.
 
Example 1:
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:
Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
Example 3:
Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
"""
def isReversible(num):
    # Function to reverse an integer
    def reverse(n):
        return int(str(n)[::-1])
    
    # Reverse num to get reversed1
    reversed1 = reverse(num)
    
    # Reverse reversed1 to get reversed2
    reversed2 = reverse(reversed1)
    
    # Return True if reversed2 equals num, otherwise False
    return reversed2 == num

# Example usage:
print(isReversible(526))  # Output: True
print(isReversible(1800))  # Output: False
print(isReversible(0))     # Output: True

