class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        pairs = {"]":"[","}":"{",")":"("}
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif char in "]})":
                if not stack or stack[-1] not in pairs[char]:
                    return False 
                else:
                    stack.pop() 
        return len(stack) == 0      