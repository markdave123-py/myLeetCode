class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [x for x in s]
        frq = Counter(arr)
        count = list(frq.values())
        res = 0
        for i in range(len(count)):
            if count[i] % 2 == 0:
                res += count[i]
            else:
                res += count[i]-1
        return res if len(arr) == res else res+1
