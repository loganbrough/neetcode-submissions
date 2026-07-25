from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = 1
        R = 1
        L_arr = [0] * len(nums)
        R_arr = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1
            L_arr[i] = L
            R_arr[j] = R
            L *= nums[i]
            R *= nums[j]
        
        return [l*r for l, r in zip(L_arr, R_arr)]
