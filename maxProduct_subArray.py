class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = max(nums)

        minEle = 1
        maxEle = 1
        
        for num in nums:
            temp = minEle * num
            minEle = min(minEle * num, maxEle * num, num)
            maxEle = max(temp, maxEle * num, num)
            
            res = max(res, maxEle)
        return res