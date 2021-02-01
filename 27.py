class Solution:
    def removeElement(self, nums, val: int):
        nums.sort()
        sI = None
        eI = None
        for i in range(len(nums)):
            if (nums[i] == val):
                if (sI == None): 
                    sI = i
            elif(sI != None and eI == None): 
                eI = i
        return nums[:sI] + (nums[eI:] if eI else nums[len(nums):])
        
print(Solution().removeElement([3,2,2,3,4], 2))