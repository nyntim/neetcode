class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = hi
        while lo <= hi:
            k = (lo + hi) // 2
            
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time <= h:
                res = k
                hi = k - 1
            else:
                lo = k + 1
                       
        return res