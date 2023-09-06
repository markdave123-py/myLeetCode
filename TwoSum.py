class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        out = []

        for i, ele in enumerate(nums):
            if target - ele not in seen:
                seen[ele] = i
            else:
                return [seen[target - ele], i]
                

            
        
        return out
