class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 0
        unique = set(nums)
        for num in unique:
            if num - 1 not in unique:
                length = 1
                while num + length in unique:
                    length += 1
                
                longest = max(length, longest)

        return longest
