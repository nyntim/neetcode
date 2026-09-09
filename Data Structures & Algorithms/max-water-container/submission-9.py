class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        l, r = 0, length - 1
        out = 0
        while l < r:
            lh, rh = heights[l], heights[r]
            diff = r - l
            out = max(min(lh, rh) * diff, out) 
            if lh < rh: l += 1
            elif rh <= lh: r -= 1
    
        return out