# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preOrder(self, root, level,res):
      if root:
          if len(res)<level+1:
              res.append([])

          res[level].append(root.val)
          self.preOrder(root.left,level+1,res)
          self.preOrder(root.right,level+1,res)
    def levelOrderBottom(self, root):
          res=[]
          self.preOrder(root,0,res)
          res.reverse()
          return res

a = TreeNode(1)
b = TreeNode(2)
a.left = b
s = Solution()
print s.levelOrderBottom(a)