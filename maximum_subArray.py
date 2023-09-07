class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r = 0
        resSum = 0
        maxSub = nums[0]

        for n in nums:
            
            if resSum < 0:
                resSum = 0
            
            resSum += n

            maxSub = max(maxSub, resSum)
        
        

        return maxSub
        