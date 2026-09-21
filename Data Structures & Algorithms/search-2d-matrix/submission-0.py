class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            arr += row
        
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target: return True
            if target > arr[mid]: lo = mid + 1
            elif target < arr[mid]: hi = mid - 1
        
        return False