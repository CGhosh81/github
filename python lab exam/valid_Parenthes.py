"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1.	Open brackets must be closed by the same type of brackets.
2.	Open brackets must be closed in the correct order.
3.	Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true

"""
def ValidParentheses(s):
    stack = []
    for b in s:
        if b in "({[":
            stack.append(b)
        elif b in ")}]":
            if not stack:  # Check if stack is empty
                return False
            if stack[-1] == "(" and b == ")":
                stack.pop()
            elif stack[-1] == "{" and b == "}":
                stack.pop()
            elif stack[-1] == "[" and b == "]":
                stack.pop()
            else:
                return False  # Mismatched bracket
    
    # If stack is empty, parentheses are valid
    return not stack

# Test cases
print(ValidParentheses("()"))        # True
print(ValidParentheses("()[]{}"))    # True
print(ValidParentheses("(]"))        # False
print(ValidParentheses("([)]"))      # False
print(ValidParentheses("{[]}"))      # True
print(ValidParentheses("})]}"))      # True
