class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = s.lower()
        length = len(pal)
        front = 0
        end = length - 1
        while front < end:
            while front < end and not pal[front].isalnum(): front += 1
            while front < end and not pal[end].isalnum(): end -= 1
            if pal[front] != pal[end]: return False

            front += 1
            end -= 1

        return True