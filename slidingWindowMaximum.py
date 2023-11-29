# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         l = 0
#         r = k
#         output = []

#         while r <= len(nums):
#             maxN = max(nums[l:r])
#             output.append(maxN)
#             l += 1
#             r += 1

#         return output

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l = r = 0
        output = []
        q = collections.deque()

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

        return output


           # while r < len(nums):
        #     maxN = max(nums[l:r])
        #     output.append(maxN)
        #     l += 1
        #     r += 1

        # return output



