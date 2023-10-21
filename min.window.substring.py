class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # setT  = set(t)
        # l = 0
        # seen = 0
        # minRes = len(s)
        # res = ''

        # for r in range(len(s)):
        #     if s[r] in setT:
        #         seen += 1
        #         if seen == 1:
        #             start = r
                    
        #         while seen == len(t):
        #             minRes = min(minRes, r - l + 1)
        #             res = s[start: r + 1]
        #             l = r
        #             if s[l] in setT:
        #                 seen = 1
        #             seen = 0          

        # print(res, minRes)
        # return res

        if t == "": return ""
        countT , window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        seen, need = 0 ,len(countT) 
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                seen += 1
            while seen == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    seen -= 1
                l += 1 
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""

               


        