class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return max(nums)
        
        robbed=[nums[0], max(nums[0],nums[1])]
        
        for i in range(2,len(nums)):
            robbed.append(max(nums[i]+robbed[-2],robbed[-1]))
            
        return robbed[-1]