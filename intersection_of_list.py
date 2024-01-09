class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        out = {}
        outArr = []
        for num in nums1:
            if num not in out:
                out[num] = -1

            else:
                pass

        for num in nums2:
            if num in out:
                out[num] += 1

        for num in out:
            if out[num] > -1:
                outArr.append(num)

        return outArr
