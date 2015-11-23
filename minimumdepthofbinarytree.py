# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    min_depth = float('inf')
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root,1)

    def dfs(self,root,depth):
        if depth > self.min_depth:
            root.right = None
            root.left = None
        if not root.left and not root.right:
            if depth < self.min_depth:
                self.min_depth = depth
        if root.left:
            self.dfs(root.left,depth+1)
        if root.right:
            self.dfs(root.right,depth+1)
        return self.min_depth


