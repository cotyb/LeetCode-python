# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    out = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.dfs(root,str(root.val))
        return self.out

    def dfs(self,root,result):
        if not root.left and not root.right:
            self.out.append(result)
        if root.left:
            self.dfs(root.left,result+"->"+str(root.left.val))
        if root.right:
            self.dfs(root.right, result+"->"+str(root.right.val))

