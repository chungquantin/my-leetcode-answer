class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        listOfRoman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        chars = [k for k in s]
        i = 0
        while (i < len(chars)):
            cur = listOfRoman.get(chars[i])
            if (i < len(chars) - 1): 
                nex = listOfRoman.get(chars[i+1])
                if (cur * 10  == nex or cur * 5  == nex):
                    res = res + abs(cur  - nex)
                    i = i + 2
                    continue
                else: 
                    res = res + listOfRoman.get(chars[i])
            else: 
                res = res + listOfRoman.get(chars[i])
            i = i + 1
        return res

print("Result:", Solution().romanToInt('MCMXCIV'))