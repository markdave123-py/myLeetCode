class Solution:
    def minSubArrayLen(self, target, nums):
        dis = 100000000

        l, currSum = 0, 0

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                dis = min(dis, r - l + 1)
                currSum -= nums[l]
                l += 1

    
        if dis  > len(nums):
            return 0
            
        return dis