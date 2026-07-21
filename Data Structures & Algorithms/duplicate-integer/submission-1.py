from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = defaultdict(list)
        hasdupe = 0
        for n in nums:
            if n in numdict:
                hasdupe += 1
            numdict[n].append(n)
        if hasdupe == 0:
            return False
        if hasdupe > 0:
            return True


            