class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in ['{', '[', '(']:
                stack.append(char)
            elif len(stack) != 0:
                if char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif len(stack) == 0 and char in ['}', ']', ')']:
                return False
        return len(stack) == 0
