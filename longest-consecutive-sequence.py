class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        setNum = set(nums)

        candidate = set()
        for n in nums:
            if n-1 not in setNum and n+1 in setNum:
                candidate.add(n)
        
        longest = 1
        for n in candidate:
            next = n + 1
            while next in setNum:
                next += 1
            longest = max(longest, next - n)
        
        return longest