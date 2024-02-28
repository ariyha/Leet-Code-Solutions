# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d=0
        val = root.val
        visited=[]
        stack=[(root,0)]

        while(stack!=[]):
            x,curr_d = stack.pop()
            print(x.val,curr_d)
            
            if curr_d>d:
                d=curr_d
                val = x.val

            visited.append(x)
            
            if x.right!=None and x.right not in visited:
                stack.append((x.right,curr_d+1))
                visited.append(x.right)
            if x.left!=None and x.left not in visited:
                visited.append(x.left)
                stack.append((x.left,curr_d+1))
        
        return val