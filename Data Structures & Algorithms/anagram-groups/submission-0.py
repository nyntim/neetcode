class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_map = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in sorted_map:
                sorted_map[key] = [word]
            else: sorted_map[key].append(word)

        return list(sorted_map.values())