class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in key:
                stack.append(c)
            if c in key.values():
                if not stack: return False
                popped = stack.pop()
                if key[popped] != c: return False
        if stack: return False
        return True
