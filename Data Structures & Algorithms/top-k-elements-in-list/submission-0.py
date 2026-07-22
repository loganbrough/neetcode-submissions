from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        grouped_nums = defaultdict(list)
        for n in nums:
            grouped_nums[n].append(n)
        nums_collection = sorted(list(grouped_nums.values()), key=lambda x: len(x), reverse=True)
        print(nums_collection)
        for i in range(k):
            result.append(nums_collection[i][0])
        return result

        

