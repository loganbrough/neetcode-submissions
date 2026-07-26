class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = []
        

        for n in range(len(nums)):
            if nums[n] - 1 in set(nums):
                continue

            current_sequence = []
            current_num = nums[n]

            while current_num in set(nums):
                current_sequence.append(current_num)
                current_num += 1

            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
        
        return len(longest_sequence)