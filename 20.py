class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 == 1): return False
        pairs = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        listOfChars = [c for c in s]
        stack = []
        for char in listOfChars: 
            if (char in pairs.keys()): 
                stack.append(char)
            else: 
                if (stack and pairs.get(stack[-1]) == char):
                    stack.pop(-1)
                else: 
                    return False
        return len(stack) == 0
        
        
print(Solution().isValid("){"))