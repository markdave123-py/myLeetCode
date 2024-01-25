class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        setT = set()

        for a in t:
            setT.add(a)

        for ele in s:
            setT.remove(ele)

        print(setT)
