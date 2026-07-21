from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = defaultdict(list)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsdict:
                return [numsdict[diff], i]
            numsdict[num] = i