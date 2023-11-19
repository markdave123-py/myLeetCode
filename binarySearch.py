class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,h = 0, len(nums)-1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] < target:
                l = mid + 1

            elif nums[mid] > target:
                h = mid - 1

            else:
                return mid

        return -1
        