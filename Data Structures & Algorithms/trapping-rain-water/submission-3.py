class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 0
        max_l, max_r = [0]*len(height), [0]*len(height)

        for i in range(len(height)):
            j = -i - 1
            max_l[i], max_r[j] = l, r
            l = max(l, height[i])
            r = max(r, height[j])

        water = 0

        for i in range(len(height)):
            water += max(0, min(max_l[i],max_r[i]) - height[i])

        return water
            
            