'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s):
    closeOpen = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = [] 

    for char in s:
        if char in closeOpen:
            if stack and stack[-1] == closeOpen[char]:
                stack.pop()
            else:
                return False 
        else:
            stack.append(char)
        
    return len(stack) == 0

print(isValid("(){}[]"))
# The inner most valid parentheses will be closed off by its counterpart
# immediately. We can use this behaviour to build a stack. If the stack is
# empty and we come across a closing parentheses, then we know that this is 
# invalid. If the stack is not empty then we just look at the previous opening
# parenthes and if it matches, then we pop off this pair. If the parentheses is 
# an opening parentheses then we just append to the stack. If the string is valid 
# then the stack will be empty since no parentheses will be unclosed

# Time | Space: O(n) | O(n)