class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
        
        
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))