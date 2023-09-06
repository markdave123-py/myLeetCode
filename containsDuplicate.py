class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        freq = {}

        for i,ele in enumerate(nums):
            
            if ele in freq:
                freq[ele] += 1

            else:
                freq[ele] = 1

        if (len(freq) == len(nums)):
            return False

        else:
            return True
        