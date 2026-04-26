class Solution:
    def rob(self, nums: List[int]) -> int:
        me=[-1]*len(nums)
        def dfs(i):
            if i>=len(nums):
                return 0
            if me[i]!=-1:
                return me[i]
            me[i]=max(dfs(i+1),nums[i]+dfs(i+2))
            return me[i]
        return dfs(0)