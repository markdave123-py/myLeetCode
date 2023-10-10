class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        import re

        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print(cleaned_s)

        c_s = cleaned_s.replace(" ", "")

        return c_s == c_s[::-1]