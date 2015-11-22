# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = []
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            return self.dfs(root,0)

    def dfs(self,root,depth):
        if len(self.result) <= depth:
            self.result.append([])
        self.result[depth].append(root.val)
        if root.left:
            self.dfs(root.left, depth+1)
        if root.right:
            self.dfs(root.right, depth+1)
        return self.result