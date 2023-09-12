class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            #we are in the left portion
            if target == nums[m]:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1

                else:
                    r = m -1

            #we in the right portion
            else:
                if target > nums[r] or target < nums[m]:
                    r = m -1
                else: 
                    l = m + 1

        return -1
        