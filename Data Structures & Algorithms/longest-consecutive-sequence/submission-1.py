class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = []
        all_nums = set(nums)

        for n in range(len(nums)): #O(n)
            if nums[n] - 1 in all_nums:
                continue

            current_sequence = []
            current_num = nums[n]

            while current_num in all_nums: #O(1)
                current_sequence.append(current_num)
                current_num += 1

            if len(current_sequence) > len(longest_sequence): #O(1)
                longest_sequence = current_sequence
        
        return len(longest_sequence) #soln should be O(n)?