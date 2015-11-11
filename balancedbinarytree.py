# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.getDepth(root) != -1

    def get_Depth(self, root):
        if root == None:
            return 0
        else:
            l = self.get_Depth(root.left)
            r = self.get_Depth(root.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return (1 + max(l, r))