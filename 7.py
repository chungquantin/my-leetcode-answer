class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = None
        if (x >= 0):
            if (''.join([k for k in str(x)[::-1]]) == ''.join([k for k in str(x)])):
                return True
        return False 
            
    
print(Solution().isPalindrome(121))