class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        win = {}
        max_freq = 0

        for r in range(len(s)):
            win[s[r]] = win.get(s[r], 0) + 1
            max_freq = max(max_freq, win[s[r]])

            window_len = r - l + 1
            if window_len - max_freq > k:
                win[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res