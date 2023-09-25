class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        dp = [0] * (n + 1)
        most_significant = 1

        for i in range(1, n+1):
            if most_significant * 2 == i:
                most_significant = i
            dp[i] = 1 + dp[i - most_significant]

        return dp


        