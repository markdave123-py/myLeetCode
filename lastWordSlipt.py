class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        stripped = s.strip()
        print(stripped)
        strList = stripped.split(" ")
        print(strList)
        return len(strList[-1])
