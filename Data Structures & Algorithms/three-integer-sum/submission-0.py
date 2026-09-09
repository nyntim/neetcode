class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate values for i

            seen = set()
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                if target in seen:
                    triplet = [nums[i], nums[j], target]
                    if triplet not in out:
                        out.append(triplet)
                seen.add(nums[j])

        return out