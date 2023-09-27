class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        
        return Counter(s) == Counter(t) 

        
        
        
        
        
        
        
        
        
        # if len(s) != len(t):
        #     return False 

        # seenS, seenT = {}, {}

        # for i in range(len(s)):
        #     seenS[s[i]] = 1 + seenS.get(s[i], 0)
        #     seenT[t[i]] = 1 + seenT.get(t[i], 0)

        # for c in seenS:
        #     if seenS[c] != seenT.get(c, 0):
        #         return False

        # return True

        # for ele in s:
        #     seen[ele] += 1

        # print(seen)

        # for ele_ in t:
        #     if ele_ in seen:
        #         seen[ele_] -= 1
        #         if seen[ele_] < 0:
        #             return False

        #     # else:
        #     #     return False
        # print(seen)
        

        # return sum(seen.values()) == 0
        


## ! ALL ANSWERS ARE CORRECT