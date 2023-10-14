class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
       
        for i, num in enumerate(numbers):
            # diff = target - num
            if target - num not in seen:
                seen[num] = i

            else:
                return [seen[target - num] + 1, i + 1]