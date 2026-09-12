class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        length = len(s)
        while r < length:
            temp = s[l:r]
            rcurr = s[r]
            if rcurr not in temp: r += 1
            else:
                l += 1
            res = max(res, r - l)

        return res



