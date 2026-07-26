class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = 1
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1
            l_arr[i] = l
            r_arr[j] = r
            l *= nums[i]
            r *= nums[j]
        
        return [l*r for l,r in zip(l_arr, r_arr)]