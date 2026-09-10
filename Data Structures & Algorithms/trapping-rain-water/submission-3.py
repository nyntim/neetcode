class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_wall, right_wall = height[left], height[right]
        trapped = 0

        while left < right:
            if left_wall < right_wall:
                left += 1
                left_wall = max(left_wall, height[left])
                trapped += left_wall - height[left]
            else:
                right -= 1
                right_wall = max(right_wall, height[right])
                trapped += right_wall - height[right]

        return trapped