from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s)) #ie act, cat turn into act, act so we now have ["sorted","sorted",..]
            anagram_dict[sorted_s].append(s)
        return list(anagram_dict.values())