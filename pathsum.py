# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    root_leaf = True
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root,sum,0)

    def dfs(self,root,sum,curSum):
        if not root:
            return False
        elif not root.left and not root.right:
            return curSum + root.val == sum
        else:
            return self.dfs(root.left,sum,curSum+root.val) or self.dfs(root.right,sum,curSum+root.val)

