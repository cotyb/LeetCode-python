#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = []
    ksamll = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root, k)
        return self.res[-1]

    def inorder(self,root,k):
        if root == None:
            return
        if len(self.res) == k:
            print self.res[-1]
            return self.res[-1]
        self.inorder(root.left,k)
        self.res.append(root.val)
        self.inorder(root.right,k)

a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
d = TreeNode(4)
# a.left = b
# a.right = c
# c.right = d
b.right = a
so = Solution()
print so.kthSmallest(b, 2)