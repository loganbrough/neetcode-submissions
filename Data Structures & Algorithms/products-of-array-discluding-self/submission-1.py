from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = 1
        R = 1
        pre = [0] * len(nums)
        post = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1
            pre[i] = L
            post[j] = R
            L *= nums[i]
            R *= nums[j]
        
        return [l*r for l, r in zip(pre, post)]
