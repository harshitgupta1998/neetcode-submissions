class Solution:
    def rob(self, nums: List[int]) -> int:
         return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
        newr=0
        rob1=0
        rob2=0
        for i in nums:
            newr=max(rob1+i,rob2)
            rob1=rob2
            rob2=newr
        return rob2
            