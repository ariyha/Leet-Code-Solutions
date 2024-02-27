# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def size(root):
            if root==None:
                return 0
            
            r = size(root.right)
            l = size(root.left)
            res[0] = max(res[0],r+l)

            return max(r,l)+1
        
        size(root)
        return res[0]