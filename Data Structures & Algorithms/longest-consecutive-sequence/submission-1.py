class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = set(nums)
        keys = sorted(unique)

        length = 1
        lengths = []
        prev = keys[0]

        for key in keys[1:]:
            if key == prev + 1:
                length += 1
            else:
                lengths.append(length)
                length = 1
            prev = key

        lengths.append(length)
        return max(lengths)