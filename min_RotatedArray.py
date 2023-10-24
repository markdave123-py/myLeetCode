class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        l, h = 0, len(nums) -1
        

        while l <= h:
            if nums[l] < nums[h]:
                res = min(res, nums[l])
                break
            mid = (l + h) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1

            else:
                h = mid -1

        return res

            

            


        