class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        l = 0

        r = len(temperatures)
        out = []

        while l < r:
            for i, ele in enumerate(temperatures[l:]):
                print(i)
                if temperatures[l] < ele:
                    out.append(i)
                    break

            else:
                out.append(0)

            l += 1
        res = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
