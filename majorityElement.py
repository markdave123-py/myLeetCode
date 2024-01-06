class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = {}

        for ele in nums:
            if ele not in freq:
                freq[ele] = 1
            else:
                freq[ele] += 1

        # val = max(freq.values())
        # return next(key for key,value in freq.items() if value == val)
        high = 0
        ans = {}
        for ele in freq:
            ans[freq[ele]] = ele
            high = max(high, freq[ele])
        return ans[high]
