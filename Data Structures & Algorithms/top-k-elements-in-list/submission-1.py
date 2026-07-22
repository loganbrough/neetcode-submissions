from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0) #For every appearance of count[n] in nums, add 1 to count[n]'s value
                                          #Now we have "1": "# times 1 appears", "2": "# times 2 appears", etc.
        for n, c in count.items():
            frequency[c].append(n)
        print(frequency)
        result = []
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]: #Takes each number from each frequency and adds it in descending order to result. If empty adds nothing
                result.append(n)
                if len(result) == k:
                    return result


        

