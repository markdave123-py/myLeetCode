class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = 0
        r = k
        output = []

        while r <= len(nums):
            maxN = max(nums[l:r])
            output.append(maxN)
            l += 1
            r += 1

        return output
