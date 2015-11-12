# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#the test case can be 1,2,2,#,3,3 and 1,2,3,3,#,2,#
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.is_Symmetric(root.left, root.right)

    def is_Symmetric(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            if left.val == right.val:
                return self.is_Symmetric(left.right, right.left) and self.is_Symmetric(left.left, right.right)
            else:
                return False

