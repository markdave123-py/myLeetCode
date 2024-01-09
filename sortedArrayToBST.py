# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: TreeNode
        # """
        numLen = len(nums)
        if not numLen:
            return None

        midNode = numLen // 2

        return TreeNode(
            nums[midNode], self.sortedArrayToBST(nums[:midNode]),
            self.sortedArrayToBST(nums[midNode + 1:]))
