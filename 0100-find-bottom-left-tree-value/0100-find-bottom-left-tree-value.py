# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        val = root.val
        stack=[root]

        while(stack!=[]):
            x = stack.pop(0)
            
            val = x.val
                     
            if x.right!=None:
                stack.append(x.right)
            if x.left!=None:
                stack.append(x.left)

        return val