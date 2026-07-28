class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {')':'(',']':'[','}':'{'}
        stack = []

        for i in s:
            if i in valid_pairs:
                if stack and stack[-1] == valid_pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return stack == []