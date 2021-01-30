class Solution:
    def merge(self, intervals : list):
        sortedInterval = sorted(intervals, key = lambda x: x[0] )
        merged = []
        for interval in sortedInterval: 
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else: 
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

print(Solution().merge([[1,4],[0,4]]) )
                        
                    