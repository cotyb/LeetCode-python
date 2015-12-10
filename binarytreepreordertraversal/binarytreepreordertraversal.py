# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return self.res
        self.dfs(root)
        return self.res

    def dfs(self,root):
        self.res.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
