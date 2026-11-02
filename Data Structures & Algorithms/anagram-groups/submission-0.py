from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            sorted_key = tuple(sorted(str))
            map[sorted_key].append(str)
        
        return list(map.values())