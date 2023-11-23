class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        seen = {}

        for i, temp in enumerate(temperatures):
            seen[temp] = i

        print(seen)
